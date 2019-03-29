import os
from foodkm import config
from elasticsearch import Elasticsearch

from flask import Flask, jsonify, request
from flask_cors import CORS

import logging

from foodkm.geo_utils import get_latitude_longitude_google_api

app = Flask(__name__)
CORS(app)

es = Elasticsearch(
    [os.environ['FOODKM_ES_HOST']],
    scheme="http",
    port=os.environ['FOODKM_ES_PORT']
)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def make_search_query(query, lat, lon, fields):
    return {
        "size": 50,
        "_source": True,
        "script_fields": {
                "distance": {
                    "script": {
                        "lang": "painless",
                        "source": "doc['location'].arcDistance(params.lat,params.lon)",
                        "params": {
                            "lat": float(lat),
                            "lon": float(lon)
                        }
                    }
                }
        },
        "query": {
            "bool": {
                # "must_not": {
                #     {
                #         "range": {
                #             "location.lat": {
                #                 "gte": -0.01, "lte": 0.01
                #             }
                #         }
                #     }
                # },
                "filter": {
                    "multi_match": {
                        "fields": fields,
                        "query": query,
                        "type": 'cross_fields',
                        # "fuzziness": "0",
                        "operator": "and"
                    }
                },
                "should": [
                    {
                        "term": {
                            "product_name": {
                                "value": query,
                                "boost": 1.0
                            }
                        }
                    },
                    {
                        "term": {
                            "category_child2": {
                                "value": query,
                                "boost": 1.0
                            }
                        }
                    }
                ]
            }
        },
        # "sort": [
        #     {
        #         "price": "asc"
        #     }
        # ],
        "suggest": {
            "suggestions": {
                "text": query,
                "term": {
                    "suggest_mode": "popular",
                    "min_word_length": 3,
                    "field": "product_name",
                    "size": 5,
                }
            }
        }
    }


def parse_search_result(hit):
    distance = hit['fields']["distance"][0] / 1000
    co2 = distance * 10
    return {**hit['_source'], 'distance': distance, 'co2': co2}


def parse_search_results(results):
    hits = results['hits']['hits']
    suggest = results['suggest']['suggestions']
    if suggest:
        suggest = suggest[0]['options']
    return [parse_search_result(h) for h in hits], suggest


@app.route("/search")
def search():
    req_args = ['query', 'lat', 'lon']
    query_args = {ra: request.args.get(ra) for ra in req_args}
    query = make_search_query(**query_args, fields=["product_description", "category_child1", "category_child2", "product_name"])
    results = es.search(index="food_in_km", doc_type="_doc", body=query)
    # if len(results['hits']['hits']) < 2:
    #     query = make_search_query(**query_args, fields=["category_child1", "category_child2",  "product_name"])
    #     results = es.search(index="food_in_km", doc_type="_doc", body=query)
    results, suggest = parse_search_results(results)
    body = {'results': results, 'suggest': suggest}
    return jsonify(body)


def get_user_location(postal_code):
    address = postal_code + " " + config.USER_COUNTRY
    log.info(config.GOOGLE_MAPS_API_KEY)
    log.info(address)
    geodata = get_latitude_longitude_google_api(
        config.GOOGLE_MAPS_API_URL, config.GOOGLE_MAPS_API_KEY, address)
    log.info(geodata)
    return geodata['lat'], geodata['lon'], geodata['address']


@app.route("/location")
def location():
    user_geo_location = {}
    try:
        lat, lon, address = get_user_location(request.args.get('query'))
        user_geo_location['lat'] = lat
        user_geo_location['lon'] = lon
        user_geo_location['address'] = address

        return jsonify(user_geo_location)
    except Exception as exp:
        return jsonify({'error': str(exp)})


def run():
    app.run(debug=True)
