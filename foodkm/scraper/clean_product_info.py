import requests
import pandas as pd
import numpy as np
import config
import argparse
from foodkm.app.geo_utils import get_latitude_longitude_google_api


def update_column_names(df, COL_RENAME_DICT):
      df_ = df.copy()
  return df_.rename(columns=config.COL_RENAME_DICT)


def clean_and_rename(df):
    # Drop non necesary columns
    df_selection = df.drop(col_drops, axis=1)

    # Manage ingredients into a new data structure and select only unique
    df_ingred = df_selection[col_ingredients]

    # criteria cleaning regex ingredients
    df_selection = df_selection.drop(col_ingredients, axis=1)
    df_ingred['ingredients'] = df_ingred[col_ingredients[0]] + '. ' +  df_ingred[col_ingredients[1]] + '. ' +\
                                            df_ingred[col_ingredients[2]] + '. ' + df_ingred[col_ingredients[3]]

    df_selection.loc[:,'ingredients'] = df_ingred['ingredients'].str.replace('"','').str.replace("'",'').str.replace('[','').str.replace(']','')\
                                                            .str.replace(':','').str.replace('\.\.','\.').str.replace('^\. ','').str.replace('^ ','')\
                                                            .str.replace('\\','').str.lower().tolist()

    # Rename columns
    return update_column_names(df_selection, COL_RENAME_DICT)

def extract_prices_info(df):
    # Get price netto and quantity as different columns
    df['price'] = df['price'].str.replace(',','.').astype(float)
    df['price_netto'] = df['price_norm'].str.split(':').str[1]
    df['product_price_netto'] = df['price_netto'].str.split(' ').str[1].str.replace(',','.').astype(float)
    df['product_quantity_netto'] = df['price_norm'].str.split(':').str[0].replace('unknown', np.nan)
    return df.drop(['price_norm','price_netto'], axis=1)


def get_lat_long_from_address(df):
    lats = []
    longs = []
    for address in df['provider_address'].tolist():
    try:
        lat, long = get_latitude_longitude_google_api(GOOGLE_MAPS_API_URL, GOOGLE_MAPS_API_KEY, address)
    except Exception as exp: 
        print("{} not valid because {}".format(address, exp))
        lat = 0
        long = 0
        
    lats.append(lat)
    longs.append(long)

    df['lat'] = lats
    df['longs'] = longs

    return df


def main(input):
    df = pd.read_csv(input)

    # clean product info
    df_clean = clean_and_rename(df)

    # format net prices
    df_complete = extract_prices_info(df_clean)

    # Get latitude/longitude
    df_geo_complete = get_lat_long_from_address(df_complete)

    # Save final csv
    clean_df.to_csv(config.final_product_info_clean, index=False, encoding='utf-8')

if __name__ == "__main__":
    parser.add_argument('input', help='path to input csv file')
    args = parser.parse_args()

    main(args.input)