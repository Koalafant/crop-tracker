from weather import weather_caller
from world_gen import world
from weather import geocoder
from weather import timezone_lookup as tz

class Handler:

    def get_lat_lon(self, var):
        return geocoder.query(var)

    def get_weather(self, lat, lon):
        return weather_caller.query(lat, lon)

    def run(self):
        while True:
            print('Enter a city: ', end='')
            try:
                lat, lon = self.get_lat_lon(input())
                self.get_weather(lat, lon)
                print(tz.get_utc_offset(lat,lon))
            except SyntaxError:
                print('Invalid city!')
                continue


this = Handler()
this.run()