import requests 
import json

api_url = 'https://github.com/toddmotto/public-apis/blob/master/LICENSE'

response = requests.get(api_url)
results = response.json()

json.loads(results)