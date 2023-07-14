from weather import weather_caller
from world_gen import world
from weather import geocoder
from weather import timezone_lookup as tz
from weather import soil_lookup
class Handler:

    def __init__(self):
        self.lat = None
        self.lon = None
        self.timezone_offset = None

    def get_lat_lon(self, var):
        return geocoder.query(var)

    def get_weather(self, lat, lon):
        return weather_caller.query(lat, lon)

    def run(self):
        while True:
            print('Enter a city: ', end='')
            try:
                self.lat, self.lon = self.get_lat_lon(input())
                self.get_weather(self.lat, self.lon)
                self.timezone_offset = tz.get_utc_offset(self.lat,self.lon)
                soil_lookup.query(self.lat, self.lon)
            except SyntaxError:
                print('Invalid city!')
                continue


this = Handler()
this.run()
