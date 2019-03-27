import os
from elasticsearch import Elasticsearch

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


es = Elasticsearch(
    [os.environ['FOODKM_ES_HOST']],
    scheme="http",
    port=os.environ['FOODKM_ES_PORT']
)

print('FOODKM_ES_HOST', os.environ['FOODKM_ES_HOST'])

def make_search_query(category_child1, lat, lon):
    return {
        "sort": [
            {
                "_geo_distance": {
                    "location": [int(lat), int(lon)],
                    "order": "asc",
                    "unit": "km",
                    "mode": "min",
                    "distance_type": "arc",
                    "ignore_unmapped": "true"
                }
            }
        ],
        "query": {
            "match": {"category_child1": category_child1}
        }
    }


def parse_search_result(hit):
    distance = hit['sort'][0]
    co2 = distance * 10
    return {**hit['_source'], 'distance': distance, 'co2': co2}


def parse_search_results(results):
    hits = results['hits']['hits']
    return [parse_search_result(h) for h in hits]


@app.route("/search")
def search():
    req_args = ['category_child1', 'lat', 'lon']
    query_args = {ra: request.args.get(ra) for ra in req_args}
    query = make_search_query(**query_args)
    results = es.search(index="food_in_km", doc_type="_doc", body=query)
    results = parse_search_results(results)
    body = {'results': results}
    return jsonify(body)


def run():
    app.run(debug=True)
