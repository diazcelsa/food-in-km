import re
import time
import os
import pandas as pd
from bs4 import BeautifulSoup

from foodkm.scraper.scrape_utils import login, switch_to_menu


# Generate product ids of interest
# ROOT_ELEMS = ['#elemT107', '#elemT128', '#elemT137', '#elemT295', '#elemT409', '#elemT456', '#elemT617'] #'#elemT8',
ROOT_IDS = [110, 128, 137, 295, 409, 456, 617] #8,
ROOT_CATS = [
    # 'PASCUA',
    # 'BAJADAS PVP',
    # 'NOVEDADES',
    # 'SUSHI',
    'ALIMENTACION',
    'APERITIVOS',
    'BEBES',
    'BEBIDAS',
    'CARNES',
    'CHARCUTERIA',
    'COMPLEMENTOS DE HOGAR',
    'CONGELADOS',
    # 'DROGUERIA',
    'FRUTAS Y VERDURAS',
    'HORNO Y BOLLERIA',
    'LACTEOS, BEBIDAS Y POSTRES VEGETALES',
    # 'MASCOTAS',
    # 'PERFUMERIA',
    'PESCADERIA'
]


def parse_html(rest, id_elem=None, category_1=None, category_2=None,
               category_3=None, category_4=None, category_5=None, category_6=None):

    soup_cat = BeautifulSoup(rest, "html.parser")
    tbody = soup_cat.findAll('tbody')
    tbody = tbody[0]
    trs = tbody.findAll('tr')

    dicts = []

    # print('one an a half')
    for tr in trs:
        aha = tr.findAll('td', {'headers':'header2'})
        # print('two')
        if len(aha[0]) != 0 and len(aha[0].findAll('a')) != 0:
            # print('three')
            product_id = re.findall(r'\d+', aha[0].findAll('a')[0]['href'])[0]

            spans = aha[1].findAll('span')
            if len(spans) == 0:
                price = 'unknown'
                price_norm = 'unknown'
            elif len(spans) == 1:
                price = spans[0].text
                price_norm = 'unknown'
            elif len(spans) == 2:
                price = spans[0].text
                price_norm = spans[1].text
            dict_info = {
                'root_cat': category_1,
                'child_1_cat': category_2,
                'child_2_cat': category_3,
                'child_3_cat': category_4,
                'child_4_cat': category_5,
                'child_5_cat': category_6,
                'product_id': product_id,
                'id_elem': id_elem,
                'price': price,
                'price_norm': price_norm
            }
            dicts.append(dict_info)
            # print(dicts)
    return dicts


def get_main_html(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame("mainFrame")
    return driver.execute_script('return document.documentElement.outerHTML')


def collect_ids(driver, id_elem, **categories):
    print(f"collect id {id_elem}")
    got_first_page = False
    dicts = []
    while True:
        if not got_first_page:
            switch_to_menu(driver)
            elems = driver.find_elements_by_css_selector(f'#{id_elem} a')
            assert len(elems) == 1, 'Expected exactly one element.'
            elems[0].click()
            rest = get_main_html(driver)
            try:
                dicts.extend(parse_html(rest, id_elem=id_elem, **categories))
                got_first_page = True
            except Exception as exp:
                print(rest)
                time.sleep(60)
        else:
            driver.switch_to.default_content()
            driver.switch_to.frame("mainFrame")
            next_page = driver.find_elements_by_css_selector('#NEXT')
            if not next_page:
                break
            next_page[0].click()

            rest = get_main_html(driver)
            try:
                dicts.extend(parse_html(rest, id_elem=id_elem, **categories))
            except Exception as exp:
                print(rest)
                driver.back()
                time.sleep(60)
    return dicts


def find_menu_children(driver, parent, level):
    category = parent.text.split('\n')[0]
    parent_link = parent.find_elements_by_css_selector('a')

    assert len(parent_link) == 1, 'Expected only one child link.'

    parent_link[0].click()

    # get third children
    children = parent.find_elements_by_css_selector(f'.ulnivel{level} li')
    return category, children


def single_menu_children(driver, id_elem, **categories):
    df_products = collect_ids(driver, id_elem, **categories)

    switch_to_menu(driver)
    time.sleep(8)
    return df_products


def make_file_name(category_1=None, category_2=None):
    clean_cat1 = category_1.replace(" ", "")
    clean_cat2 = category_2.replace(" ", "")
    return f"data/product_ids/{clean_cat1}__{clean_cat2}.csv"


def check_df(category_1=None, category_2=None):
    filename = make_file_name(category_1, category_2)
    return os.path.isfile(filename)


def store_df(records, category_1=None, category_2=None):
    filename = make_file_name(category_1, category_2)
    df = pd.DataFrame.from_records(records).reset_index(drop=True)
    df.to_csv(filename, index=False, encoding="utf-8")


def get_all_ids():
    driver = login()
    switch_to_menu(driver)

    # Extract product Ids
    dfs_products = []

    parents = driver.find_elements_by_css_selector(f'.ulnivel1 li')

    for first_level in parents:
        id_elem = first_level.get_attribute('id')

        # open root
        parent_category, children_one = find_menu_children(
            driver, first_level, level=2)

        if parent_category not in ROOT_CATS:
            print(f'Skip category {parent_category}')
            continue
        else:
            print(f'Scrape category {parent_category}')

        if len(children_one) == 0:
            dfs_products.extend(single_menu_children(
                driver, id_elem, category_1=parent_category))
            continue

        else:
            # open first children
            for child_one in children_one:
                children_one_category, children_two = find_menu_children(driver, child_one, level=3)
                if check_df(category_1=parent_category, category_2=children_one_category):
                    print(f'Skip subcategory {children_one_category}')
                    continue

                if len(children_two) == 0:
                    id_elem = child_one.get_attribute('id')
                    dfs_products.extend(single_menu_children(
                        driver, id_elem, category_1=parent_category, category_2=children_one_category))
                    continue

                else:
                    # open second children
                    for child_two in children_two:
                        children_two_category,  children_three = find_menu_children(driver, child_two, level=4)
                        if len(children_three) == 0:
                            id_elem = child_two.get_attribute('id')
                            dfs_products.extend(single_menu_children(
                                driver, id_elem, category_1=parent_category, category_2=children_one_category,
                                category_3=children_two_category))
                            continue

                        else:
                            # open thrid children
                            for child_three in children_three:
                                children_three_category,  children_four = find_menu_children(
                                    driver, child_three, level=5)
                                if len(children_four) == 0:
                                    id_elem = child_three.get_attribute('id')
                                    dfs_products.extend(single_menu_children(
                                        driver, id_elem, category_1=parent_category, category_2=children_one_category,
                                        category_3=children_two_category, category_4=children_three_category))
                                    continue

                                else:
                                    # open four children
                                    for child_four in children_four:
                                        children_four_category,  children_five = find_menu_children(
                                            driver, child_four, level=6)
                                        id_elem = child_four.get_attribute('id')
                                        dfs_products.extend(single_menu_children(
                                            driver, id_elem, category_1=parent_category, category_2=children_one_category,
                                            category_3=children_two_category, category_4=children_three_category,
                                            category_5=children_four_category))

                print(f'Store {parent_category} || {children_one_category}')
                store_df(dfs_products, category_1=parent_category, category_2=children_one_category)
                dfs_products = []
    driver.close()


def main():
    get_all_ids()


if __name__ == "__main__":
    main()
