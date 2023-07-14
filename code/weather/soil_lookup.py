import requests
import json

# use of soilgrids.org api to determine likely soil content

url = 'https://rest.isric.org/soilgrids/v2.0/properties/query'#?lon=-112.5762841&lat=34.6405789&property=clay&property=nitrogen&property=sand&property=silt&depth=0-5cm&depth=5-15cm&value=mean'
def query(lat, lon):
    params = {
        'lat' : lat,
        'lon' : lon,
        'property' : ['clay', 'nitrogen', 'sand', 'silt'],
        'depth' : ['0-5cm', '5-15cm'],
        'value' : ['mean']
    }

    request = requests.get(url, params)
    data = json.loads(request.text)['properties']['layers']
    #clay
    print(data[0])
    #sand
    print(data[2])
    # silt
    print(data[3])
    #nitrogen
    print(data[1])