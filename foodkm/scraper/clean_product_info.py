import pandas as pd
import numpy as np
from foodkm import config
import os


def update_column_names(df, COL_RENAME_DICT):
    df_ = df[list(COL_RENAME_DICT.keys()) + ['ingredients'] + config.PRICES + config.LOCATION_COL].copy()
    return df_.rename(columns=COL_RENAME_DICT)


def clean_and_rename(df):
    # Drop non necesary columns
    # df_selection = df.drop(config.COL_DROPS, axis=1)

    # Manage ingredients into a new data structure and select only unique
    df_ingred = df[config.COL_INGREDIENTS].copy()

    # criteria cleaning regex ingredients
    # df_selection = df_selection.drop(config.COL_INGREDIENTS, axis=1)
    df_ingred['ingredients'] = df_ingred[config.COL_INGREDIENTS[0]] + '. ' + df_ingred[
        config.COL_INGREDIENTS[1]] + '. ' + \
                               df_ingred[config.COL_INGREDIENTS[2]] + '. ' + df_ingred[config.COL_INGREDIENTS[3]]

    df.loc[:, 'ingredients'] = df_ingred['ingredients'].str.replace('"', '').str.replace("'", '').str.replace('[',
                                                                                                              '').str.replace(
        ']', '') \
        .str.replace(':', '').str.replace('\.\.', '\.').str.replace('^\. ', '').str.replace('^ ', '') \
        .str.replace('\\', '').str.lower().tolist()

    # Rename columns
    return update_column_names(df, config.COL_RENAME_DICT)


def extract_prices_info(df):
    # Get price netto and quantity as different columns
    df['price'] = pd.to_numeric(df['price'].str.replace(',', '.'), errors='coerce')
    w_p_null = df['price'].isnull()
    w_pn_null = df['price_norm'].isnull()
    df.loc[w_p_null & ~w_pn_null, 'price_norm'] = df.loc[w_p_null & ~w_pn_null, 'price']
    df['price_netto'] = df['price_norm'].str.split(':').str[1]
    df['product_price_netto'] = \
        df['price_netto'].str.split(' ').str[1].str.replace(',', '.').astype(float)
    df['product_quantity_netto'] = \
        df['price_norm'].str.split(':').str[0].replace('unknown', np.nan)
    df.drop(['price_norm', 'price_netto'], axis=1)
    return df


def get_paths(source):
    basename, ext = os.path.splitext(source)
    source_path = f"data/product_geo/{source}"
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

        # Save final csv
        df_complete.to_csv(dest, index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
