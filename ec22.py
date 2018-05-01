import boto3


#variables
backup_tag= "AMI_Backup_Policy"

client = boto3.client('ec2')
dynamodb = boto3.client('dynamodb')
response = client.describe_instances(Filters=[{'Name': 'tag-key','Values':[backup_tag]}])
instancelist = []
timelist = []
for reservation in response['Reservations']:
        instance = reservation['Instances'][0]['InstanceId']
        amiresponse = client.create_image(InstanceId=instance, Name="test-nikil"+ instance)
        client.create_tags(
        Resources=[
            amiresponse['ImageId'],
        ],
        Tags=[
        {
            'Key': 'Auto-Backup',
            'Value': 'yes',
        },
        ],
        )
 
        dynamodb.put_item(
	TableName = 'ami_backup_policy',
	Item={'ami_ids' :{
		'S': amiresponse['ImageId'],
		}
	})
        for n in reservation['Instances'][0]['Tags']:
                print n
                if n['Key'] == backup_tag :
                    b=n["Value"]
                    c=b.split("-")
                    timelist.append(c[0])

print instance

print timelist
