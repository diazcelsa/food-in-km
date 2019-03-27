import time
import os
import pandas as pd
from bs4 import BeautifulSoup

from foodkm.scraper.scrape_utils import get_driver


def get_product_info(all_product_ids):

    # access my mercadona account
    driver = get_driver()

    contenidos = []
    factor = 1
    for prod_id in all_product_ids:
        while True:
            try:
                contenido = get_contenido_product(driver, prod_id)
                contenidos.append(contenido)
                print("Add product id", prod_id)
                time.sleep(2)
                factor = 1
                break
            except Exception as exp:
                driver.close()
                driver = get_driver()
                print("Server not responding: ", exp)
                factor *= 2
                time.sleep(60 * factor)

    driver.close()
    return contenidos


def get_contenido_product(driver, product_id):
    url = "https://www.telecompra.mercadona.es/detall_producte.php?id={}".format(product_id)
    driver.get(url)

    rest = driver.execute_script('return document.documentElement.outerHTML')

    soup_cat = BeautifulSoup(rest, "html.parser")
    return soup_cat.findAll('div', {'class':'contenido'})[0].decode()


def get_paths(source):
    basename, ext = os.path.splitext(source)
    source_path = f"data/product_ids/{source}"
    dest_path = f"data/product_html/{basename}.pkl"
    return source_path, dest_path


def get_all_product_id_files():
    for source in os.listdir('data/product_ids'):
        if source != 'placeholder.txt':
            source, dest = get_paths(source)
            if not os.path.isfile(dest):
                yield source, dest


def main():
    for source, dest in get_all_product_id_files():
        df = pd.read_csv(source)
        # df = df.iloc[:5]
        df['contenidos'] = get_product_info(df['product_id'].tolist())
        df.to_pickle(dest)


if __name__ == "__main__":
    main()
