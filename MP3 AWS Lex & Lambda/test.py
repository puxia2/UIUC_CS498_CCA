import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-autograder-2022-spring"

payload = {
	"graphApi": "https://fiv4klcb5d.execute-api.us-east-1.amazonaws.com/test", #<post api for storing the graph>,
	"botName": "distance_chatter", # <name of your Amazon Lex Bot>, 
	"botAlias": "distance_lex", # <alias name given when publishing the bot>,
	"identityPoolId": "us-east-1:049b3e2f-81fc-4ef0-9612-8d5cc13e00a4", #<cognito identity pool id for lex>,
	"accountId": "956926367040", #<your aws account id used for accessing lex>,
	"submitterEmail": "puxia2@illinois.edu", # <insert your coursera account email>,
	"secret": "PmwVsQ7XD12kEJFs", # <insert your secret token from coursera>,
	"region": "us-east-1" #<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)