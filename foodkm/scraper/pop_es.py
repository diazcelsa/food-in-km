import json
import pandas as pd
import os
import datetime
from elasticsearch import Elasticsearch
from pkg_resources import resource_filename

es = Elasticsearch(
    [os.environ['FOODKM_ES_HOST']],
    scheme="http",
    port=os.environ['FOODKM_ES_PORT']
)


def load_json():
    product_file = resource_filename(__name__, 'df/products.json')
    with open(product_file, 'r') as f:
        return json.load(f)


def parse_location(sr):
    return {'lat': sr.lat, 'lon': sr.lon}


def import_es(filename):
    products = pd.read_csv(filename)
    products['location'] = products[['lat', 'lon']].apply(parse_location, axis=1)
    products = products.drop(['lat', 'lon'], axis=1)
    products['date_inserted'] = datetime.datetime.now()
    for index, row in products.iterrows():
        body = row.to_dict()
        body = {k: v for k, v in body.items() if not pd.isna(v)}
        try:
            res = es.index(index="food_in_km", doc_type='_doc', body=body)
        except:
            print(body)
            import ipdb; ipdb.set_trace()
            break


def get_all_files():
    for source in os.listdir('data/product_complete'):
        if source[0].isupper():
            source = f"data/product_complete/{source}"
            yield source


def import_all():
    for filename in get_all_files():
        try:
            import_es(filename)
        except:
            break


if __name__ == "__main__":
    import_all()
