import requests
import json

# use of soilgrids.org api to determine likely soil content

url = 'https://rest.isric.org/soilgrids/v2.0/properties/query'


def query(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'property': ['clay', 'nitrogen', 'sand', 'silt'],
        'depth': ['0-5cm'],
        'value': ['mean']
    }

    request = requests.get(url, params)
    data = json.loads(request.text)['properties']['layers']
    ret = {}

    # grabs mean values for clay, nitrogen, sand and silt
    for lis in data:
        ret[lis['name']] = lis['depths'][0]['values']['mean']
    return ret
