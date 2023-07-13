import datetime
import pytz
from tzwhere import tzwhere as tz

test_lat, test_lon = '47.5048851', '-111.29189'

# given valid lat and long coords, will return time offset from UTC
def get_utc_offset(lat, lon):
    tzwhere = tz.tzwhere()
    timezone_str = tzwhere.tzNameAt(float(lat), float(lon))
    timezone = pytz.timezone(timezone_str)
    return int(datetime.datetime.now(timezone).strftime('%z')) / 100
