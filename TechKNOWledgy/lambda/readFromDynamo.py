import boto3
from boto3.dynamodb.conditions import Key, Attr


def read_ddb(dct: dict):
    # dynamodb = boto3.resource('dynamodb')
    age = dct["age"]
    race = dct["race"]
    gender = dct["gender"]
    opp = dct["opportunity"]
    
    # return items
    
    # 1. Assume the AWS resource role using STS AssumeRole Action
    sts_client = boto3.client('sts')
    assumed_role_object=sts_client.assume_role(RoleArn="arn:aws:iam::154526019951:role/AFE_Hackathon", RoleSessionName="AssumeRoleSession1")
    credentials=assumed_role_object['Credentials']

    # 2. Make a new DynamoDB instance with the assumed role credentials
    dynamodb = boto3.resource('dynamodb',
                      aws_access_key_id=credentials['AccessKeyId'],
                      aws_secret_access_key=credentials['SecretAccessKey'],
                      aws_session_token=credentials['SessionToken'],
                      region_name='us-east-1')
    
    table = dynamodb.Table('AFE_Hackathon')
    
    response = table.scan(FilterExpression=Attr('age').eq(age) & Attr('race').eq(race) & Attr('gender').eq(gender) & Attr('resource_type').eq(opp))
    items = response['Items']
    
    return items

"""
    response = client.get_item(
    TableName='string',
    Key={
        'string': {
            'S': 'string',
            'N': 'string',
            'B': b'bytes',
            'SS': [
                'string',
            ],
            'NS': [
                'string',
            ],
            'BS': [
                b'bytes',
            ],
            'M': {
                'string': {'... recursive ...'}
            },
            'L': [
                {'... recursive ...'},
            ],
            'NULL': True|False,
            'BOOL': True|False
        }
    },
    AttributesToGet=[
        'string',
    ],
    ConsistentRead=True|False,
    ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
    ProjectionExpression='string',
    ExpressionAttributeNames={
        'string': 'string'
    }
"""