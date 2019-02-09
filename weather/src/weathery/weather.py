import os
import sys
import json
import requests
from weathery import table
from argparse import ArgumentParser
from veryprettytable import VeryPrettyTable

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
	args = create_parser().parse_args()
	url = make_api_url(args)
	res =  requests.get(url)
	if res.status_code != 200:
		print(f'Error reaching the weather provider: {res.status_code}')
		sys.exit(1)
	data = res.json()
	weather_state = table.table(data)
	print(weather_state)
			
if __name__ == '__main__':
	main()