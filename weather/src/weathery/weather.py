import os
import sys
import json
import requests
from argparse import ArgumentParser
from veryprettytable import VeryPrettyTable


HEADERS = ['City', 'Temperature', 'Condition', 'Details']

def make_api_url(args):
	api_key = os.getenv('OWM_API_KEY')
	if not api_key:
		print('Error: OWM API KEY NOT FOUND -> EXPORT API KEY AS ENV VARIABLE')
		sys.exit(1)
	api_url = f"https://api.openweathermap.org/data/2.5/weather?q={args.city},{args.country}&appid={api_key}"
	return api_url

def create_parser():
	parser = ArgumentParser(description='Get the current weather information for your city')
	parser.add_argument('city', help='name of city to get weather for')
	parser.add_argument('country', help='country code the city belongs to')
	return parser

def main():
	x = VeryPrettyTable()
	args = create_parser().parse_args()
	url = make_api_url(args)
	res =  requests.get(url)
	if res.status_code != 200:
		print(f'Error reaching the weather provider: {res.status_code}')
		sys.exit(1)
	data = res.json()
	x.field_names = ['City', 'Temperature', 'Forcast', 'Details']
	x.add_row([data["name"],data["main"]["temp"],data["weather"][0]["main"],data["weather"][0]["main"]])

	print(x)
			
if __name__ == '__main__':
	main()