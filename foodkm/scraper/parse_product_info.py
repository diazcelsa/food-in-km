import os
import math
import pandas as pd
import itertools
from bs4 import BeautifulSoup


def extract_structured_product_info(all_product_info):
    # convert string to bs4 object
    indexes = all_product_info.index.tolist()

    df_all_contenidos_complete = []
    for index in indexes:
        soup_cat = BeautifulSoup(str(all_product_info.loc[index,'contenidos']), "html.parser")
        products_collector = []
        names_info = [i.text for i in soup_cat.findAll('dt')]
        values_info = [i.text for i in soup_cat.findAll('dd') if i.text != '']
        nunique_names = len(list(set(names_info)))
        if nunique_names == 0:
            continue

        repetitions = math.ceil(len(names_info)/nunique_names)

        if repetitions > 1:
            product_info = {}
            product_info = define_product_general_info_object(product_info, all_product_info, index)

            for j, name in enumerate(names_info):

                # product name
                one = soup_cat.find('div', {'class': 'inter'}).text.split(':')
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
                for name, value in zip(names_info, values_info):
                    product_info[name] = value

            product_info = get_additional_info_product(soup_cat, product_info)
            products_collector.append(product_info)
        df_all_contenidos_complete.append(products_collector)

    # shape all data as dataframe
    clean_df = pd.DataFrame.from_records(itertools.chain.from_iterable(df_all_contenidos_complete))
    return clean_df


def define_product_general_info_object(product_info, dataset, index):
    product_info['child_1_cat'] = dataset.loc[index,'child_1_cat']
    product_info['child_2_cat'] = dataset.loc[index,'child_2_cat']
    product_info['child_3_cat'] = dataset.loc[index,'child_3_cat']
    product_info['child_4_cat'] = dataset.loc[index,'child_4_cat']
    product_info['child_5_cat'] = dataset.loc[index,'child_5_cat']
    product_info['price'] = dataset.loc[index,'price']
    product_info['price_norm'] = dataset.loc[index,'price_norm']
    product_info['product_id'] = dataset.loc[index,'product_id']
    product_info['root_cat'] = dataset.loc[index,'root_cat']
    return product_info



def get_additional_info_product(soup_cat, product_info):
    # ingredients
    alerg = soup_cat.find('div', {'id':'tabla_ingredientes_alergenos'})
    if alerg:
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


def get_paths(source):
    basename, ext = os.path.splitext(source)
    source_path = f"data/product_html/{source}"
    dest_path = f"data/product_info/{basename}.csv"
    return source_path, dest_path


def get_all_product_html_files():
    for source in os.listdir('data/product_html'):
        if source != 'placeholder.txt':
            source, dest = get_paths(source)
            if not os.path.isfile(dest):
                yield source, dest


def main():
    for source, dest in get_all_product_html_files():
        df = pd.read_pickle(source)
        clean_df = extract_structured_product_info(df)
        clean_df.to_csv(dest, index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
