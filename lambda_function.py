import json
import boto3
import random
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ShortUrls')

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    method = event['requestContext']['http']['method']
    path = event['rawPath'].strip('/')

    if method == 'POST' and path == 'shorten':
        body = json.loads(event['body'])
        long_url = body['url']
        short_id = generate_id()
        table.put_item(Item={'id': short_id, 'url': long_url})
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({'id': short_id})
        }

    elif method == 'GET':
        short_id = path
        response = table.get_item(Key={'id': short_id})
        if 'Item' in response:
            return {
                'statusCode': 302,
                'headers': { 'Location': response['Item']['url'] }
            }
        else:
            return {
                'statusCode': 404,
                'body': 'URL not found'
            }
