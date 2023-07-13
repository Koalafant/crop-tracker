import requests
import json

url = 'https://geocode.maps.co/search?'#street=555+5th+Ave&city=New+York&state=NY&postalcode=10017&country=US'


def query(q):
    # params = {
    #     'street': street.replace(' ', '+'),
    #     'city': city.replace(' ', '+'),
    #     'state': state.replace(' ', '+'),
    #     'postalcode': postalcode.replace(' ', '+'),
    #     'country': country.replace(' ', '+'),
    # }
    q = q.replace(',', '')#.replace(' ', '+')
    params = {
        'q' : q
    }
    request = requests.get(url, params)
    data = json.loads(request.text)
    print(f"Latitude: {data[0]['lat']}; Longitude: {data[0]['lon']}")
    return data[0]['lat'], data[0]['lon']
