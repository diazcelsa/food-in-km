import re
import os
import time
import pickle
import numpy as np
import pandas as pd
import requests
import itertools
from bs4 import BeautifulSoup
from selenium import webdriver

# Generate product ids of interest
ROOT_ELEMS = ['#elemT107', '#elemT128', '#elemT137', '#elemT295', '#elemT409', '#elemT456', '#elemT617'] #'#elemT8', 
ROOT_IDS = [107, 128, 137, 295, 409, 456, 617] #8, 


def collect_ids(driver, id_elem, category_1='none', category_2='none', category_3='none', category_4='none',
                category_5='none', category_6='none'):
    try:
        print("before open2")
        elems = driver.find_elements_by_css_selector('#elemT'+ str(id_elem))
        if isinstance(elems, list):
            print(elems, type(elems))
            elems[0].click()
        else:
            print("are u inside?")
            elems.click()
        # id_elem += 1
        print("after open2")

        # check if more than one page
        dicts = []
        next_page_option = True
        while next_page_option == True:

            # move to the menu frame to extract product ids and prices
            driver.switch_to.default_content()
            driver.switch_to.frame("mainFrame")
            rest = driver.execute_script('return document.documentElement.outerHTML')
            soup_cat = BeautifulSoup(rest, "html.parser")
            print('one')
            tbody = soup_cat.findAll('tbody')
            if isinstance(tbody, list):
                print("really", tbody, type(tbody))
                tbody = tbody[0]
            trs = tbody.findAll('tr')

            # collect product ids and prices
            product_ids = []
            prices = []
            print('one an a half')
            for tr in trs:
                aha = tr.findAll('td', {'headers':'header2'})
                print('two')
                if len(aha[0]) != 0 and len(aha[0].findAll('a')) != 0:
                    print('three')
                    product_ids.append(re.findall(r'\d+', aha[0].findAll('a')[0]['href'])[0])
                    if len(aha[1]) != 0 and len(aha[1].findAll('span', 
                                                               {'class': 'precio_ud tdcenter'})) != 0:
                        print('four')
                        prices.append(aha[1].findAll('span', {'class': 'precio_ud tdcenter'})[0].text)
                    else:
                        prices.append('unknown')

            # Save info in df
            for i, product_id in enumerate(product_ids):
                dict_info = {
                    'root_cat': category_1,
                    'child_1_cat': category_2,
                    'child_2_cat': category_3,
                    'child_3_cat': category_4,
                    'child_4_cat': category_5,
                    'child_5_cat': category_6,
                    'product_id': product_id,
                    'price': prices[i]
                }
                dicts.append(dict_info)
                # print(f'Example dict_info {dict_info}')
            next_page = driver.find_elements_by_css_selector('#NEXT')

            if len(next_page) != 0:
                time.sleep(5)
                #import pdb; pdb.set_trace()
                next_page = driver.find_elements_by_css_selector('#NEXT')
                print('five')
                next_page[0].click()
                # driver.switch_to.default_content()
                # driver.switch_to.frame("mainFrame")
            else:
                next_page_option = False
        return pd.DataFrame.from_dict(dicts)
                
    except Exception as exp:
        print(f'Error with id {id_elem}: {exp}')
        time.sleep(10)
        return pd.DataFrame.from_dict([{
                    'root_cat': category_1,
                    'child_1_cat': category_2,
                    'child_2_cat': category_3,
                    'child_3_cat': category_4,
                    'child_4_cat': category_5,
                    'child_5_cat': category_6,
                    'product_id': '',
                    'price': ''
                }])


def get_contenido_product(product_id):
    url = "https://www.telecompra.mercadona.es/detall_producte.php?id={}".format(product_id)
    driver.get(url)

    rest = driver.execute_script('return document.documentElement.outerHTML')
    soup_cat = BeautifulSoup(rest, "html.parser")
    return soup_cat.findAll('div', {'class':'contenido'})[0]


def get_additional_info_product(soup_cat, product_info):
    # ingredients
    alerg = soup_cat.find('div', {'id':'tabla_ingredientes_alergenos'})
    bool_alerg = alerg.find('dt')
    if bool_alerg:
        bool_alerg = bool_alerg.text
        alergenic_ing = alerg.findAll('dd')
        if len(alergenic_ing) != 0:
            ingrdts = [i.findAll('b') for i in alergenic_ing][0]
            product_info['Alérgenos'] = [i.text for i in ingrdts]
            product_info[bool_alerg] = [i.text for i in alergenic_ing][0].split(',')

    # complementary info
    if soup_cat.find('div', {'id':"tabla_información_complementaria"}):
        complementary = soup_cat.find('div', {'id':"tabla_información_complementaria"})
        if complementary.find('dt'):
            compl_names = complementary.find('dt')
            compl_values = complementary.find('dd')
            print(compl_names)
            for i, name in enumerate(compl_names):
                product_info[name.text] = compl_values[i]
            
    return product_info

def define_product_general_info_object(product_info, dataset, index):
    product_info['child_1_cat'] = dataset.loc[index,'child_1_cat']
    product_info['child_2_cat'] = dataset.loc[index,'child_2_cat']
    product_info['child_3_cat'] = dataset.loc[index,'child_3_cat']
    product_info['child_4_cat'] = dataset.loc[index,'child_4_cat']
    product_info['child_5_cat'] = dataset.loc[index,'child_5_cat']
    product_info['price'] = dataset.loc[index,'price']
    product_info['product_id'] = dataset.loc[index,'product_id']
    product_info['root_cat'] = dataset.loc[index,'root_cat']
    return product_info


def login():
    print("start extraction of product_ids")
    # Log In
    driverLocation = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(driverLocation)
    url = "https://www.telecompra.mercadona.es/ns/principal.php"
    driver.get(url)
    aqui = driver.find_elements_by_css_selector('.marcotexto a')
    aqui[0].click()

    user = driver.find_elements_by_css_selector('#username')
    user[0].send_keys(os.environ["MERCADONA_USER"])

    passw = driver.find_elements_by_css_selector('#password')
    passw[0].send_keys(os.environ["MERCADONA_PASS"])

    submit = driver.find_elements_by_css_selector('#ImgEntradaAut')
    submit[0].click()

    return driver


def switch_to_menu(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame("toc")
    driver.switch_to.frame("menu")


def find_menu_children(driver, parent, level):
    print("before open1")
    category = parent.text.split('\n')[0]
    parent.click()
    print("after open1")
    # id_elem += 1

    # get third children
    children = driver.find_elements_by_css_selector(f'.ulnivel{level} li')
    return category, children


def single_menu_children(driver, id_elem, **categories):
    print(f"collect ids, id_elem: {id_elem}, categories: {str(categories)}")
    # categories = {f'category_{i}': c for i, c in enumerate(categories)}
    df_products = collect_ids(driver, id_elem, **categories)
    # id_elem += 1
    
    switch_to_menu(driver)
    time.sleep(8)
    return df_products


# def get_from_all_children(driver, parent, level, categories, id_elem):
#     parent_category, children = find_menu_children(
#         driver, parent, level=level)
#     id_elem += 1
#     categories = categories + [parent_category]
#     if len(children) == 0:
#         dfs_products, id_elem = single_menu_children(driver, id_elem, categories)
#         continue
#     else:
#         dfs_products = []
#         for child in children:
#             child_df, id_elem = get_from_all_children(driver, child, level+1, categories, id_elem)
#             dfs_products.extend(child_df)
#     return dfs_products, id_elem


def get_all_ids():
    driver = login()
    switch_to_menu(driver)

    # Extract product Ids
    dfs_products = []
    for i, root in enumerate(ROOT_ELEMS):
        id_elem = ROOT_IDS[i]
        first_level = driver.find_elements_by_css_selector(root)

        # open root
        print(root)
        parent_category, children_one = find_menu_children(
            driver, first_level[0], level=2)

        if len(children_one) == 0:
            dfs_products.append(single_menu_children(
                driver, id_elem, category_1=parent_category))
            continue
            
        else:
            # open first children
            # if id_elem == 8:
            #     id_elem = 24
            id_elem += 1
            for child_one in children_one:
                children_one_category, children_two = find_menu_children(driver, child_one, level=3)

                if len(children_two) == 0:
                    print("mytest",children_one_category)
                    dfs_products.append(single_menu_children(
                        driver, id_elem, category_1=parent_category, category_2=children_one_category))
                    id_elem += 1
                    continue
                    
                else:
                    # open second children
                    id_elem += 1
                    for child_two in children_two:
                        children_two_category,  children_three = find_menu_children(driver, child_two, level=4)
                        if len(children_three) == 0:
                            print("mytest",children_two_category)
                            dfs_products.append(single_menu_children(
                                driver, id_elem, category_1=parent_category, category_2=children_one_category,
                                category_3=children_two_category))
                            id_elem += 1
                            continue
                            
                        else:
                            # open thrid children
                            id_elem += 1
                            for child_three in children_three:
                                children_three_category,  children_four = find_menu_children(
                                    driver, child_three, level=5)
                                if len(children_four) == 0:
                                    dfs_products.append(single_menu_children(
                                        driver, id_elem, category_1=parent_category, category_2=children_one_category,
                                        category_3=children_two_category, category_4=children_three_category))
                                    
                                    id_elem += 1
                                    continue
                                    
                                else:
                                    # open four children
                                    id_elem += 1
                                    for child_four in children_four:
                                        children_four_category,  children_five = find_menu_children(
                                            driver, child_four, level=6)
                                        dfs_products.append(single_menu_children(
                                            driver, id_elem, category_1=parent_category, category_2=children_one_category,
                                            category_3=children_two_category, category_4=children_three_category,
                                            category_5=children_four_category))

                                        id_elem += 1

        pd.concat(dfs_products).reset_index(drop=True).to_csv('mercadona_product_ids_'+ root + '.csv',
                                                            index=False,encoding="utf-8")
        time.sleep(60)
    all_product_ids = pd.concat(dfs_products).reset_index(drop=True).to_csv('mercadona_product_ids_complete.csv',
                                                            index=False,encoding="utf-8")
    driver.close()
    return all_product_ids


def get_product_info(all_product_ids):

    # access my mercadona account
    driver = login()

    contenidos = []
    for prod_id in all_product_ids['product_id'].tolist():
        while True:
            try:
                contenido = get_contenido_product(prod_id)
                print(prod_id, '\n')
                print(contenido, '\n')
                
                contenidos.append(contenido)
                time.sleep(8)
                continue
            except Exception as exp:
                print("Server not responding: ", exp)
                time.sleep(60)

    driver.close()
    return contenidos

def extract_structured_product_info(all_product_info):
    # convert string to bs4 object
    indexes = all_product_info.index.tolist()

    df_all_contenidos_complete = []
    for index in indexes:
        soup_cat = BeautifulSoup(str(all_product_info.loc[index,'contenidos']), "html.parser")
        products_collector = []
        names_info = [i.text for i in soup_cat.findAll('dt')]
        values_info = [i.text for i in soup_cat.findAll('dd') if i.text != '']
        repetitions = math.ceil(len(names_info)/len(list(set(names_info))))

        if repetitions > 1:
            product_info = {}
            product_info = define_product_general_info_object(product_info, all_product_info, index)
            
            for j, name in enumerate(names_info):
                
                # product name
                one = soup_cat.find('div', {'class':'inter'}).text.split(':')
                product_info[one[0]] = one[1]

                if j == 0:
                    product_info[name] = values_info[j]
                elif j == len(names_info)-1:
                    products_collector.append(product_info)

                elif j > 0 and name == names_info[0]:
                    product_info = get_additional_info_product(soup_cat, product_info)
                    products_collector.append(product_info)
                    #import pdb; pdb.set_trace()
                    product_info = {}
                    product_info = define_product_general_info_object(product_info, all_product_info, index)

                elif j > 0 and name != names_info[0]:
                    product_info[name] = values_info[j]

        else:
            product_info = {}
            product_info = define_product_general_info_object(product_info, all_product_info, index)
                    
            # product name
            one = soup_cat.find('div', {'class':'inter'}).text.split(':')
            product_info[one[0]] = one[1]

            # basic information
            names_info = [i.text for i in soup_cat.findAll('dt')]
            values_info = [i.text for i in soup_cat.findAll('dd')]
            if names_info:
                for i, name in enumerate(names_info):
                    product_info[name] = values_info[i]

            product_info = get_additional_info_product(soup_cat, product_info)
            products_collector.append(product_info)
        df_all_contenidos_complete.append(products_collector)
        
    # shape all data as dataframe
    sample_clean_all_products = pd.DataFrame.from_records(itertools.chain.from_iterable(df_all_contenidos_complete))
    sample_clean_all_products.to_csv('product_vector_complete.csv', index=False, encoding='utf-8')


def main():
    # Extract mercadona product ids (#try/except)
    df = get_all_ids()
        # df = pd.read_csv('mercadona_product_ids_i.csv')

    # Get the HTML content of each of the food products
    df['contenidos'] = get_product_info(df['product_id'].tolist())

    # Extract cleaned product info and save all the information
    extract_structured_product_info(df)


if __name__ == "__main__":
    main()
