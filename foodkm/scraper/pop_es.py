import json
import os
from elasticsearch import Elasticsearch
from pkg_resources import resource_filename

es = Elasticsearch(
    [os.environ['FOODKM_ES_HOST']],
    http_auth=('user', 'secret'),
    scheme="https",
    port=os.environ['FOODKM_ES_PORT'],
)

def load_json():
    product_file = resource_filename(__name__, 'sample/products.json')
    with open(product_file, 'r') as f:
        return json.load(f)


def import_es():
    products = load_json()
    for p in products:
        res = es.index(index="food_in_km", doc_type='product', body=p, id=1)
        print(res)


if __name__ == "__main__":
    import_es()
