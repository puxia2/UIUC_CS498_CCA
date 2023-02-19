from collections import defaultdict
import json
import boto3


def lambda_handler(event, context):
    src = event['currentIntent']['slots']['source']
    des = event['currentIntent']['slots']['destination']

    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    tableDistance = dynamodb.Table('shortest_distance')

    try:
        row = tableDistance.get_item(
            Key={
                'source': src,
                'destination': des
            }
        )
        distance = int(row['Item']['distance'])

        response = {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "SSML",
                    "content": "{dis}".format(dis=distance)
                },
            }
        }
        return response
    
    except:
        print("Encounter error!")
        response = {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "SSML",
                    "content": "Error!"
                },
            }
        }
        return response