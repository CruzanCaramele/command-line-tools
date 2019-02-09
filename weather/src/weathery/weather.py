import os
import sys
import json
import requests
from tabulate import tabulate
from argparse import ArgumentParser

weather_state = []
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
	args = create_parser().parse_args()
	url = make_api_url(args)
	res =  requests.get(url)
	if res.status_code != 200:
		print(f'Error reaching the weather provider: {res.status_code}')
		sys.exit(1)
	data = res.json()
	#print(f'{json.dumps(data, sort_keys=True, indent=4)}')
	weather_state.append(f'{data["name"]}')
	weather_state.append(f'{data["main"]["temp"]}') 
	weather_state.append(f'{data["weather"][0]["main"]}')
	weather_state.append(f'{data["weather"][0]["description"]}')
	# print(weather_state)
	# print(tabulate(weather_state, headers=HEADERS))

	print(tabulate({"City": weather_state[0], "Temperature": weather_state[1]}, headers="keys"))
	


if __name__ == '__main__':
	main()