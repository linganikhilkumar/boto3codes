import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.get_item(
    TableName='ami_backup_policy',
    Key = {
        'ami_ids': {
            'S': '01',
            }
         })
#for i  in response['Item']['AMI_IDS']: 
             
res2 = response['Item']['AMI_IDS']['L']
for i  in res2:
   
