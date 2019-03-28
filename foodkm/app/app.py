import os
from foodkm import config
from elasticsearch import Elasticsearch

from flask import Flask, jsonify, request
from flask_cors import CORS

from foodkm.geo_utils import get_latitude_longitude_google_api

app = Flask(__name__)
CORS(app)

es = Elasticsearch(
    [os.environ['FOODKM_ES_HOST']],
    scheme="http",
    port=os.environ['FOODKM_ES_PORT']
)

def make_search_query(query, lat, lon):
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
            "multi_match": {
                "fields": ["product_name"],
                "query": query,
                "fuzziness": "AUTO"
            }
        },
        "suggest": {
            "suggestions": {
                "text": query,
                "term": {
                    "field": "product_name"
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
    return [parse_search_result(h) for h in hits], suggest


@app.route("/search")
def search():
    req_args = ['query', 'lat', 'lon']
    query_args = {ra: request.args.get(ra) for ra in req_args}
    query = make_search_query(**query_args)
    results = es.search(index="food_in_km", doc_type="_doc", body=query)
    results, suggest = parse_search_results(results)
    body = {'results': results, 'suggest': suggest}
    return jsonify(body)


def get_user_location(postal_code):
    address = postal_code + ", " + config.USER_COUNTRY
    geodata = get_latitude_longitude_google_api(
        config.GOOGLE_MAPS_API_URL, config.GOOGLE_MAPS_API_KEY, address)
    return geodata['lat'], geodata['lon']


@app.route("/location")
def location():
    user_geo_location = {}
    lat, lon = get_user_location(request.args.get('postal_code'))
    user_geo_location['lat'] = lat
    user_geo_location['lon'] = lon
    return jsonify(user_geo_location)


def run():
    app.run(debug=True)
