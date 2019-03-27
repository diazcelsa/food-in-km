import json
import os
from elasticsearch import Elasticsearch
from pkg_resources import resource_filename

es = Elasticsearch(
    [os.environ['FOODKM_ES_HOST']],
    scheme="http",
    port=os.environ['FOODKM_ES_PORT'],
)

def load_json():
    product_file = resource_filename(__name__, 'df/products.json')
    with open(product_file, 'r') as f:
        return json.load(f)


def import_es():
    products = load_json()
    for p in products:
        res = es.index(index="food_in_km", doc_type='_doc', body=p)
        print(res)


if __name__ == "__main__":
    import_es()
