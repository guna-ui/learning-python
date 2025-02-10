import requests
import json


url="https://jsonmock.hackerrank.com/api/football_matches"

response=requests.get(url)


print(response.json())