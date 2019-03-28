import os
import pandas as pd


def get_all_product_id_files():
    for source in os.listdir('data/product_info'):
        if source[0].isupper():
            s_file = f'data/product_info/{source}'
            yield s_file


def main():
    dfs = []
    for source in get_all_product_id_files():
        df = pd.read_csv(source)
        dfs.append(df)
    all_df = pd.concat(dfs)
    # Save final csv
    dest_path = f"data/product_info_all.csv"
    all_df.to_csv(dest_path, index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
