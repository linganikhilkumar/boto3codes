import boto3


#variables
backup_tag= "AMI_Backup_Policy"

client = boto3.client('ec2')
response = client.describe_instances(Filters=[{'Name': 'tag-key','Values':[backup_tag]}])
instancelist = []
timelist = []
for reservation in response['Reservations']:
	instance = reservation['Instances'][0]['InstanceId']
        AMIid = client.create_image(InstanceId=instance, Name="nikhil-ami-"+instance)
        for n in reservation['Instances'][0]['Tags']:
                print n
		if n['Key'] == backup_tag :
                    b=n["Value"]
                    c=b.split("-")
                    timelist.append(c[0])

print instance

print timelist

