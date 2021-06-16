import json
import boto3
import os

users_table =os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def getMovie(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-1]
    response = table.get_item(
        Key={
            'pk': user_id,
            'sk': 'profile'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def putMovie(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-1]
    
    body=json.loads(event["body"])
    print(body)
    print(user_id)
    
    table.put_item(
        Item={
            'pk': user_id,
            'sk':'profile',
            'title': body["title"],
            'main_actor': body["main_actor"],
            'year': body["year"]
        }
    )   
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getMovieByRoomPerson(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-3]+path.split("/")[-1]
    
    body=json.loads(event["body"])
    print(body)
    print(user_id)
    
    table.put_item(
        Item={
            'pk': user_id,
            'sk':'date_'
        }
    )   
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    
def putMovieByRoomPerson(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-3]+path.split("/")[-1]
    
    
    body=json.loads(event["body"])
    list_or_people=body["listPersons"];
    print(body)
    print(user_id)
    
    
    table.put_item(
        Item={
            'pk': user_id,
            'sk': body["date_id"],
            'person': body["listPersons"]
        }
    )
        
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
def getCinemaSchedule(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-3]+path.split("/")[-1]
    response = table.get_item(
        Key={
            'pk': user_id,
            'sk': 'room_'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    
def putCinemaSchedule(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-3]+path.split("/")[-1]
    
    body=json.loads(event["body"])
    print(body)
    print(user_id)
    
    table.put_item(
        Item={
            'pk': user_id,
            'sk':body["room_id"],
            'schedule': body["schedule"]
        }
    )   
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getRoom(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[1]
    response = table.get_item(
        Key={
            'pk': user_id,
            'sk': 'profile'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def putRoom(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-1]
    
    body=json.loads(event["body"])
    print(body)
    print(user_id)
    
    table.put_item(
        Item={
            'pk': user_id,
            'sk':'profile',
            'seats':body['seats'],
            '3d':body['3d']
        }
    )   
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
def getPersonMovie(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-1]
    response = table.get_item(
        Key={
            'pk': user_id,
            'sk': 'movie_id'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def putPersonMovie(event, context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-1]
    
    body=json.loads(event["body"])
    print(body)
    print(user_id)
    
    table.put_item(
        Item={
            'pk': user_id,
            'sk':body["movie_id"],
            'date': body["date"],
        }
    )   
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def putPersonRoom(event,context):
    print(json.dumps({"running":True}))
    print(json.dumps(event))
    path=event["path"]
    user_id=path.split("/")[-1]
    
    body=json.loads(event["body"])
    print(body)
    print(user_id)s