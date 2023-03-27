import requests
import json

url = 'https://u46j45y1h6.execute-api.us-east-1.amazonaws.com/prod/'

payload = {
			"submitterEmail": "puxia2@illinois.edu", # <insert your coursera account email>,
			"secret": "DIvRkKgItweblL9L", # <insert your secret token from coursera>,
			"dbApi": "https://0exrz5dvpf.execute-api.us-east-1.amazonaws.com/test" # insert your API Gateway Post method invoke URL
		}
print(json.dumps(payload))
r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
