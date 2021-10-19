import requests
from termcolor import colored

my_headers = {'User-Agent': 'Iphone 11'}
r = requests.get("http://httpbin.org", headers=my_headers)

print(r.text)