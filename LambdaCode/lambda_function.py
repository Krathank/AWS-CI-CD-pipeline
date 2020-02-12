import boto3
import json

ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    return {"statusCode": 200, "body": "Hi there,Hello from lambda. I am running in us-east-1"}
