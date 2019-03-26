import os

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_API_KEYS'].split('[')[1].split(']')[0].split(',')[0]