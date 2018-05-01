import boto3

client = boto3.client('ec2')
response = client.create_tags(
    Resources=[
        'ami-d6ef84ae',
        'ami-e9ef8491',
        'ami-e8ef8490',
    ],
    Tags=[
        {
            'Key': 'Auto-Backup',
            'Value': 'yes',
        },
    ],
)
