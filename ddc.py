import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='AMI_Backup_Policy',
    KeySchema=[
        {
            'AttributeName': 'ami-ids', 
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ami-ids', 
            'AttributeType': 'S'
        }    
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1, 
        'WriteCapacityUnits': 1
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='AMI_Backup_Policy')
print(table.item_count) 
print(table.name)       
