import requests
import json

url = '''https://api.open-meteo.com/v1/forecast'''


def query(lat, lon):
    params = {
        'latitude': lat,
        'longitude': lon,
        'hourly': 'temperature_2m,precipitation_probability,precipitation,rain,snowfall',
        'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum',
        'timezone': 'GMT'
    }

    request = requests.get(url, params)
    data = json.loads(request.text)

    # parse data later and return useful stuff
    for key in data['hourly']:
        print(key)
        print(data['hourly'][key])
