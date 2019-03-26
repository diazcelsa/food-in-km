import time
import pandas as pd
from bs4 import BeautifulSoup

from foodkm.scraper.scrape_utils import login, switch_to_menu


def get_product_info(all_product_ids):

    # access my mercadona account
    driver = login()

    contenidos = []
    for prod_id in all_product_ids:
        while True:
            try:
                contenido = get_contenido_product(driver, prod_id)
                contenidos.append(contenido)
                print("Add product id", prod_id)
                time.sleep(8)
                break
            except Exception as exp:
                print("Server not responding: ", exp)
                time.sleep(60)

    driver.close()
    return contenidos


def get_contenido_product(driver, product_id):
    url = "https://www.telecompra.mercadona.es/detall_producte.php?id={}".format(product_id)
    driver.get(url)

    rest = driver.execute_script('return document.documentElement.outerHTML')
    soup_cat = BeautifulSoup(rest, "html.parser")
    return soup_cat.findAll('div', {'class':'contenido'})[0]


def make_file_name(source):
    filename = os.path.basename(source)
    filename, ext = os.path.splitext(filename)
    return f"data/product_html/{filename}.pkl"


def check_df(category_1=None, category_2=None):
    filename = make_file_name(category_1, category_2)
    return os.path.isfile(filename)

def get_all_product_id_files():
    for source in os.listdir('data/product_ids'):
        dest = make_file_name(source)
        if not os.path.isfile(filename)


def main():


    df = pd.read_csv('data/mercadona_product_ids_#elem110.csv')
    df = df.iloc[:10]
    # Get the HTML content of each of the food products
    df['contenidos'] = get_product_info(df['product_id'].tolist())
    df.to_csv('data/mercadona_product_ids_#elem110_html.csv', index=False,encoding="utf-8")


if __name__ == "__main__":
    main()
