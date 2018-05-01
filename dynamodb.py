import boto3
import time
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr

ddb = boto3.client('dynamodb','us-west-2')

response = ddb.describe_table(
    TableName='AMI_Backup_Policy'
)

print (response)
