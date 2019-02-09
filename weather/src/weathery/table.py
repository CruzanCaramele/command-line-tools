from weathery import weather
from veryprettytable import VeryPrettyTable

HEADERS = ['City', 'Temperature', 'Forcast', 'Details']

def table(data):
	x = VeryPrettyTable()
	x.field_names = HEADERS
	x.add_row([data["name"],data["main"]["temp"],data["weather"][0]["main"],data["weather"][0]["main"]])
	return x

