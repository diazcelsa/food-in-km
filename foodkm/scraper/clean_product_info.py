import requests
import pandas as pd
import numpy as np
from foodkm import config
import argparse
import os
from foodkm.scraper.geo_utils import get_latitude_longitude_google_api


GOOGLE_MAPS_API_URL = config.GOOGLE_MAPS_API_URL
GOOGLE_MAPS_API_KEY = config.GOOGLE_MAPS_API_KEY


def update_column_names(df, COL_RENAME_DICT):
    df_ = df[list(COL_RENAME_DICT.keys()) + ['ingredients'] + config.PRICES].copy()
    return df_.rename(columns=COL_RENAME_DICT)


def clean_and_rename(df):
    # Drop non necesary columns
    # df_selection = df.drop(config.COL_DROPS, axis=1)

    # Manage ingredients into a new data structure and select only unique
    df_ingred = df[config.COL_INGREDIENTS].copy()

    # criteria cleaning regex ingredients
    # df_selection = df_selection.drop(config.COL_INGREDIENTS, axis=1)
    df_ingred['ingredients'] = df_ingred[config.COL_INGREDIENTS[0]] + '. ' +  df_ingred[config.COL_INGREDIENTS[1]] + '. ' +\
                                            df_ingred[config.COL_INGREDIENTS[2]] + '. ' + df_ingred[config.COL_INGREDIENTS[3]]

    df.loc[:,'ingredients'] = df_ingred['ingredients'].str.replace('"','').str.replace("'",'').str.replace('[','').str.replace(']','')\
                                                            .str.replace(':','').str.replace('\.\.','\.').str.replace('^\. ','').str.replace('^ ','')\
                                                            .str.replace('\\','').str.lower().tolist()

    # Rename columns
    return update_column_names(df, config.COL_RENAME_DICT)


def extract_prices_info(df):
    # Get price netto and quantity as different columns
    try:
        df['price'] = df['price'].str.replace(',','.').astype(float)
    except:
        pass
    try:
        df['price_netto'] = df['price_norm'].str.split(':').str[1]
        df['product_price_netto'] = df['price_netto'].str.split(' ').str[1].str.replace(',','.').astype(float)
        df['product_quantity_netto'] = df['price_norm'].str.split(':').str[0].replace('unknown', np.nan)
        df.drop(['price_norm','price_netto'], axis=1)
    except:
        pass
    return df



def get_lat_long_from_address(df):

    # Get all geolocation data from Google API
    lats = []
    longs = []
    addresses = []
    localities = []
    provinces = []
    states = []
    countries = []
    postal_codes = []

    for address in df['provider_address'].tolist():
        try:
            geodata = get_latitude_longitude_google_api(GOOGLE_MAPS_API_URL, GOOGLE_MAPS_API_KEY, address)
            lats.append(geodata['lat'])
            longs.append(geodata['lon'])
            addresses.append(geodata['address'])
            localities.append(geodata['locality'] if 'locality' in list(geodata.keys()) else '')
            provinces.append(geodata['province'] if 'province' in list(geodata.keys()) else '')
            states.append(geodata['state'] if 'state' in list(geodata.keys()) else '')
            countries.append(geodata['country'] if 'country' in list(geodata.keys()) else '')
            postal_codes.append(geodata['postal_code'] if 'postal_code' in list(geodata.keys()) else '')

        except Exception as exp:
            print("{} not valid because {}".format(address, exp))
            lats.append(0)
            longs.append(0)
            addresses.append(address)
            localities.append('')
            provinces.append('')
            states.append('')
            countries.append('')
            postal_codes.append('')

    df['lat'] = lats
    df['lon'] = longs
    df['address'] = addresses
    df['locality'] = localities
    df['province'] = provinces
    df['address'] = addresses
    df['state'] = states
    df['country'] = countries
    df['postal_code'] = postal_codes

    return df


def get_paths(source):
    basename, ext = os.path.splitext(source)
    source_path = f"data/product_info/{source}"
    dest_path = f"data/product_complete/{basename}.csv"
    return source_path, dest_path


def get_all_product_id_files():
    for source in os.listdir('data/product_info'):
        if source != 'placeholder.txt':
            source, dest = get_paths(source)
            if not os.path.isfile(dest):
                yield source, dest


def main():
    for source, dest in get_all_product_id_files():
        df = pd.read_csv(source)

        # clean product info
        df_clean = clean_and_rename(df)

        # format net prices
        df_complete = extract_prices_info(df_clean)

        # Get latitude/longitude
        df_geo_complete = get_lat_long_from_address(df_complete)

        # Save final csv
        df_geo_complete.to_csv(dest, index=False, encoding='utf-8')

if __name__ == "__main__":
    # parser.add_argument('input', help='path to input csv file')
    # args = parser.parse_args()

    main()
