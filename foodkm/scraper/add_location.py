import pandas as pd
import numpy as np
from foodkm import config
import os
from foodkm.geo_utils import get_latitude_longitude_google_api

GOOGLE_MAPS_API_URL = config.GOOGLE_MAPS_API_URL
GOOGLE_MAPS_API_KEY = config.GOOGLE_MAPS_API_KEY


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
    address_types = []

    for idx, row in df.iterrows():
        origen = row['Pais Origen:']
        provider = row['Dirección Proveedor:']
        if not pd.isnull(origen) and origen.lower() != 'españa':
            address = origen
            address_type = 'origin'
        else:
            address = provider
            address_type = 'supplier'

        address_types.append(address_type)
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

        # print(origen, ' ||| ' , provider, ' ||| ' ,address_type, '|||', countries[-1], '|||', row['Nombre Proveedor:'])

    df['lat'] = lats
    df['lon'] = longs
    df['address'] = addresses
    df['locality'] = localities
    df['province'] = provinces
    df['address'] = addresses
    df['address_type'] = address_types
    df['state'] = states
    df['country'] = countries
    df['postal_code'] = postal_codes

    return df


def get_paths(source):
    basename, ext = os.path.splitext(source)
    source_path = f"data/product_info/{source}"
    dest_path = f"data/product_geo/{basename}.csv"
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

        # Get latitude/longitude
        df_geo = get_lat_long_from_address(df)

        # Save final csv
        df_geo.to_csv(dest, index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
