import requests
import json

url = 'https://geocode.maps.co/search?'


def query(q):
    q = q.replace(',', '')#.replace(' ', '+')
    params = {
        'q' : q
    }
    request = requests.get(url, params)
    data = json.loads(request.text)
    print(f"Latitude: {data[0]['lat']}; Longitude: {data[0]['lon']}")
    return data[0]['lat'], data[0]['lon']
