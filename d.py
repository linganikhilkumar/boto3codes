import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.get_item(
    TableName='ami_backup_policy',
    Key={
        'ami_ids': {
            'S': ami_ids,
        }
    })
print response
