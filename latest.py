import boto3
import datetime
import sys

#variables
backup_tag= "AMI_Backup_Policy"
instancelist = []
timelist = []
#current time 

create_time = datetime.datetime.now()
#time_now = create_time.strftime("%H:%M")
time_now = '01:00'
#print time_now

client = boto3.client('ec2')
dynamodb = boto3.client('dynamodb')
response = client.describe_instances(Filters=[{'Name': 'tag-key','Values':[backup_tag]}])


for reservation in response['Reservations']:
        for n in reservation['Instances'][0]['Tags']:
                if n['Key'] == backup_tag :
                    b=n["Value"].split("-")
                    timelist.append(b[0])       
        
        instance = reservation['Instances'][0]['InstanceId']
        for time in  timelist:
            if time == time_now:

                amiresponse = client.create_image(InstanceId=instance, Name= "new-ami-"+instance)
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
                print "copying ami id "+amiresponse['ImageId']+" to Dynamo db "
                dynamodb.put_item(
                TableName = 'ami_backup_policy',
                Item={'ami_ids' :{
                'S': amiresponse['ImageId'],
                }
                })
               

       




   
