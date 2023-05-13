import time
from datetime import date, datetime, timezone
from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from geopy.geocoders import Nominatim
import pytz
import timezonefinder

class ThelemicDate:

	tf = timezonefinder.TimezoneFinder()

	numerals = ['0', 'i', 'ii', 'iii', 'iv',
				'v', 'vi', 'vii', 'viii', 'ix',
				'x', 'xi', 'xii', 'xiii', 'xiv',
				'xv', 'xvi', 'xvii', 'xviii', 'xix',
				'xx', 'xxi', 'xxii']

	signs = {'Aries': '♈', 'Taurus': '♉', 'Gemini': '♊', 'Cancer': '♋',
			 'Leo': '♌', 'Virgo': '♍', 'Libra': '♎', 'Scorpio': '♏',
			 'Sagittarius': '♐', 'Capricorn': '♑', 'Aquarius': '♒',
			 'Pisces': '♓'}

	days_of_week = ['Lunae', 'Martis', 'Mercurii', 'Jovis',
					'Veneris', 'Saturnii', 'Solis']

	def get_geopos(self, location):
		geolocator = Nominatim(user_agent="ThelemicDate")
		location = geolocator.geocode(location)
		lat, lon = float(location.latitude), float(location.longitude)
		timezone = pytz.timezone(self.tf.timezone_at(lng=lon, lat=lat))
		lat_dir = 'n' if lat >= 0 else 's'
		lon_dir = 'e' if lon >= 0 else 'w'
		lat = f"{abs(int(lat))}{lat_dir}{abs(int((lat - int(lat)) * 60))}"
		lon = f"{abs(int(lon))}{lon_dir}{abs(int((lon - int(lon)) * 60))}"
		return GeoPos(lat, lon)

	def get_timezone(self, location):
		geolocator = Nominatim(user_agent="ThelemicDate")
		location = geolocator.geocode(location)
		lat, lon = float(location.latitude), float(location.longitude)
		timezone_name = self.tf.timezone_at(lng=lon, lat=lat)
		return pytz.timezone(timezone_name)

	def now(self, location):
		pos = self.get_geopos(location)
		now = datetime.now(self.get_timezone(location))
		ve_year = int(now.strftime('%Y'))
		ve_years_total = ve_year - 1904
		cycle_i = ve_years_total // 22
		cycle_ii = ve_year - 1904 - (cycle_i * 22)
		na_year = self.numerals[cycle_i].upper() + self.numerals[cycle_ii]
		ve_weekday = now.weekday()
		ve_today = str(now.strftime('%Y/%m/%d'))
		ve_time = str(now.strftime('%H:%M'))
		na_date = Datetime(ve_today, ve_time, self.get_timezone(location).utcoffset(now.replace(tzinfo=None)).total_seconds() / 3600)
		chart = Chart(na_date, pos)
		sun = chart.getObject(const.SUN)
		solis = str(sun).split(' ')
		solis_sign = solis[1]
		solis_arc = solis[2].split(':')[0].replace('+', '')
		moon = chart.get(const.MOON)
		luna = str(moon).split(' ')
		luna_sign = luna[1]
		luna_arc = luna[2].split(':')[0].replace('+', '')
		return (f'☉ in {int(solis_arc)}º {solis_sign} : '
				f'☽ in {int(luna_arc)}º {luna_sign} : '
				f'dies {self.days_of_week[ve_weekday]} : '
				f'Anno {na_year} æræ legis')

	def in_day(self, year, month, day, hour, minute, location):
		pos = self.get_geopos(location)
		ve_weekday = date(year, month, day).weekday()
		ve_in_day_date = str(date(year, month, day).strftime('%Y/%m/%d'))
		ve_in_day_time = f'{hour}:{minute}'
		
		if month < 3 or (month == 3 and day < 20):
			ve_in_day_na_year = year - 1905  
		else:
			ve_in_day_na_year = year - 1904
		
		cycle_i = ve_in_day_na_year // 22
		cycle_ii = ve_in_day_na_year - (cycle_i * 22)
		na_year = self.numerals[cycle_i].upper() + self.numerals[cycle_ii]
		
		now = datetime.now(self.get_timezone(location))  
		na_date = Datetime(ve_in_day_date, ve_in_day_time, self.get_timezone(location).utcoffset(now.replace(tzinfo=None)).total_seconds() / 3600)
		chart = Chart(na_date, pos)
		sun = chart.getObject(const.SUN)
		solis = str(sun).split(' ')
		solis_sign = solis[1]
		solis_arc = solis[2].split(':')[0].replace('+', '')
		moon = chart.get(const.MOON)
		luna = str(moon).split(' ')
		luna_sign = luna[1]
		luna_arc = luna[2].split(':')[0].replace('+', '')
		return (f'☉ in {int(solis_arc)}º {solis_sign} : '
				f'☽ in {int(luna_arc)}º {luna_sign} : '
				f'dies {self.days_of_week[ve_weekday]} : '
				f'Anno {na_year} æræ legis')