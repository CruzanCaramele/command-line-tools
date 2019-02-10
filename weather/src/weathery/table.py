from weathery import weather
from veryprettytable import VeryPrettyTable

HEADERS = ['City', 'Temperature | Celcius', 'Temperature | Farenheit', 'Forecast', 'Details']

def celcius(temp_kelvin):
	int_temp = float(temp_kelvin)
	to_celcius = int_temp - 273.15
	return float("{0:.2f}".format(to_celcius))

def farenheit(temp_kelvin):
	int_temp = float(temp_kelvin)
	to_farenheit = (int_temp - 273.15) * 9 / 5 + 32
	return float("{0:.2f}".format(to_farenheit))

def table(data):
	x = VeryPrettyTable()
	x.field_names = HEADERS
	temp_kelvin = data['main']['temp']
	temp_celcius = celcius(temp_kelvin)
	temp_farenheit = farenheit(temp_kelvin)

	x.add_row([data['name'], temp_celcius , temp_farenheit, data['weather'][0]['main'],data['weather'][0]['description']])
	return x