from weather import weather_caller
from world_gen import world
from weather import geocoder
from weather import timezone_lookup as tz
from weather import soil_lookup
import datetime

class Handler:

    def __init__(self):
        self.lat = None
        self.lon = None
        self.timezone_offset = None
        self.soil_table = None
        self.weather_table = None

    def get_lat_lon(self, var):
        return geocoder.query(var)

    def get_weather(self, lat, lon):
        return weather_caller.query(lat, lon)

    def tz_offset(self, time, offset):
        for i, date in enumerate(time):
            offset_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
            time[i] = offset_date + datetime.timedelta(hours=offset)

    def to_farenheit(self, lis):
        for i, temp in enumerate(lis):
            lis[i] = round((float(temp)*9/5)+32, 2)

    def run(self):
        while True:
            print('Enter a city: ', end='')
            try:
                self.lat, self.lon = self.get_lat_lon(input())
                self.weather_table = self.get_weather(self.lat, self.lon)
                self.timezone_offset = tz.get_utc_offset(self.lat, self.lon)

                self.weather_table['hourly']['time'] = self.tz_offset(self.weather_table['hourly']['time'], self.timezone_offset)
                self.to_farenheit(self.weather_table['hourly']['temperature_2m'])
                self.to_farenheit(self.weather_table['daily']['temperature_2m_max'])
                self.to_farenheit(self.weather_table['daily']['temperature_2m_min'])

                self.soil_table = soil_lookup.query(self.lat, self.lon)
                print(self.soil_table)

                # TODO: compile weather and soil data into useable dict
                # TODO: compile plant database (postgres?)
                # TODO: merge weather and soil data into plant database (or join via soil and weather)
            except SyntaxError:
                print('Invalid city!')
                continue


this = Handler()
this.run()
