import requests


def get_latitude_longitude_google_api(GOOGLE_MAPS_API_URL, GOOGLE_MAPS_API_KEY, country, address):

    params = {
        'address': address,
        'sensor': 'false',
        'region': country,
        'key': GOOGLE_MAPS_API_KEY
    }

    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    result = res['results'][0]

    geodata = dict()
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']
    geodata['address'] = result['formatted_address']
    
    return geodata