import json
import pandas as pd
import os
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
    return {'lat': sr.lat, 'lon': sr.longs}


def import_es():
    products = pd.read_csv('data/sample_clean_vector.csv')
    products['location'] = products[['lat', 'longs']].apply(parse_location, axis=1)
    products = products.drop(['lat', 'longs'], axis=1)
    for index, row in products.iterrows():
        body = row.to_dict()
        body = {k: v for k, v in body.items() if not pd.isna(v)}
        print(body)
        res = es.index(index="food_in_km", doc_type='_doc', body=body)
        print(res)

if __name__ == "__main__":
    import_es()
