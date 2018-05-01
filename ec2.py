import boto3

conn = boto3.client('ec2')

lists =  conn.describe_instances()['Reservations']
#print lists['Instances']
for i in lists:
    x = i['Instances'][0]['Tags']
    for n in x:
        if n['Key'] == 'AMI_Backup_Policy':
            h=n['Value']
            t=h.split('-')
            print t[0]
            if t[0] == '02:00':
               print ('this is 2')
            
	    elif t[1] == '01:00':
               print ('these instances are having 01:00 as tag ')
	    else:
	       print('no instances') 
        
	
