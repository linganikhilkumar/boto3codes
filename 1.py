import boto3
client = boto3.client('ec2')
response = client.create_image(InstanceId='i-037fdeaf7b885c072',Name='test-image1')
print response['ImageId']


