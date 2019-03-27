import requests


def get_latitude_longitude_google_api(GOOGLE_MAPS_API_URL, GOOGLE_MAPS_API_KEY, address):

    params = {
        'address': address,
        'sensor': 'false',
        'key': GOOGLE_MAPS_API_KEY
    }

    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    if res['results']:
        result = res['results'][0]
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lon'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']

        list_address = result['address_components']
        for elem in list_address:
            if elem['types'][0] == 'locality':
                geodata['locality'] = elem['long_name']

            elif elem['types'][0] == 'administrative_area_level_2':
                geodata['province'] = elem['long_name']
            elif elem['types'][0] == 'administrative_area_level_1':
                geodata['state'] = elem['long_name']
            elif elem['types'][0] == 'country':
                geodata['country'] = elem['long_name']
            elif elem['types'][0] == 'postal_code':
                geodata['postal_code'] = elem['long_name']
        return geodata
    else:
        return None
