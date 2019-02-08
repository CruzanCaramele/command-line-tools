import os
import sys
import requests
from argparse import ArgumentParser


def make_api_url(args):
	api_key = os.getenv('OWM_API_KEY')

	if not api_key:
		print('Error: OWM API KEY NOT FOUND\
		      EXPORT API KEY AS ENV VARIABLE')
		sys.exit(1)
		url = 'https://openweathermap.org/api'

def create_parser():
	parser = ArgumentParser(description='Get the current weather information for your city')
	parser.add_argument('city', help='name of city to get weather for')
	parser.add_argument('country', help='country the city belongs to')
	return parser


def main():
	args = create_parser().parse_args()

