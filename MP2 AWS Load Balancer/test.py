import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1': '3.144.95.55:5000',  # <insert ip address:port of first EC2 instance>, 
		'ip_address2': '18.188.202.224:5000', # <insert ip address:port of secong EC2 instance>,
		'load_balancer' : 'my-alb-1509696687.us-east-2.elb.amazonaws.com', # <insert address of load balancer>,
		'submitterEmail': 'puxia2@illinois.edu', # <insert your coursera account email>,
		'secret': 'Ji1fJ4XCJRrUSK11'# <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)