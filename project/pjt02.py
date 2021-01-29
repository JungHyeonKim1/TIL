import requests
from pprint import pprint

url = 'http://api.github.com/events'

response = requests.get(url)

gith_dict = response.json()

pprint(gith_dict)