from collections import defaultdict
import json
import boto3

# input example:
# {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}
# first transform input into a dictionary like this below:
# {"Chicago": ["Urbana", "Lafayette"], "Urbana": "Springfield"}


event = {"graph": "Chicago->Urbana,Urbana->Springfield,Chicago->Lafayette"}
info = event["graph"].split(",")
trips = defaultdict(list)

for trip in info:
    trips[trip.split("->")[0]].append(trip.split("->")[1])
    trips[trip.split("->")[1]].append(trip.split("->")[0])
trips = dict(trips)
# print(trips)
# {'Chicago': ['Urbana', 'Lafayette'], 'Urbana': ['Chicago', 'Springfield'], 'Springfield': ['Urbana'], 'Lafayette': ['Chicago']}


# bfs algorithm
# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
def bfs_shortest_distance(trips, src, des): # src: starting point; des: destination
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[src]]
    # return 0 if source and destination are identical
    if src == des:
        return 0

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbors = trips[node]
            # go through all neighbor nodes, construct a new path and push it into the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # return path if neighbor is destination
                if neighbor == des:
                    return len(new_path)-1
                
            # mark node as explored
            explored.append(node)

    # if no path between two nodes, return -1
    return -1


# print(bfs_shortest_distance(trips, "Chicago", "Springfield"))

def lambda_handler(event, context):
    # instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    # instanciate the "shortest_distance" table
    tableDistance = dynamodb.Table('shortest_distance')

    # preprocessing the event (POST request)
    info = event["graph"].split(",")
    trips = defaultdict(list)

    for trip in info:
        trips[trip.split("->")[0]].append(trip.split("->")[1])
        trips[trip.split("->")[1]].append(trip.split("->")[0])
    trips = dict(trips)

    sources = list(trips.keys())

    # putting a try/catch to log to user when some error occurs
    try:
        for i in range(len(sources)):
            for k in range(len(sources)):
                src = sources[i]
                des = sources[k]
                distance = bfs_shortest_distance(trips, src, des)
                tableDistance.put_item(
                    Item = {
                        'source': src,
                        'destination': des,
                        'distance': distance
                    }
                )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }
    except:
        print('Closing lambda function')
        return {
            'statusCode': 400,
            'body': json.dumps('Error saving the distance')
        }
    