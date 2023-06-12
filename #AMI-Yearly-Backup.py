#AMI-Yearly-Backup

import boto3
import collections
import datetime
import sys
import time

ec = boto3.client('ec2')

def lambda_handler(event, context):
	
    reservations = ec.describe_instances(
	    Filters=[
		    {'Name': 'tag:Backup_Yearly', 'Values': ['yes']},
		]
	).get(
		'Reservations', []
	)

    instances = sum(
	    [
			[i for i in r['Instances']]
			for r in reservations
		], [])


    for instance in instances:
	    try:
		    retention_days = [
				int(t.get('Value')) for t in instance['Tags']
				if t['Key'] == 'Retention_'][0]
	    except IndexError:
		    retention_days = 1800
	    finally:
	    	print(retention_days)
	    	create_time = datetime.datetime.now()
	    	create_fmt = create_time.strftime('%Y-%m-%d--%H-%M-%S')
	    	AMIid = ec.create_image(InstanceId=instance['InstanceId'], Name="LambdaBackupyearly - " + instance['InstanceId'] + " from " + create_fmt, Description="Lambda created AMI of instance " + instance['InstanceId'] + " from " + create_fmt, NoReboot=True, DryRun=False)
	    	delete_date = datetime.date.today() + datetime.timedelta(days=retention_days)
	    	delete_fmt = delete_date.strftime('%d-%b-%Y')
	    	print(delete_date)
	    	time.sleep(0.10)
	    	ec.create_tags(
	    		Resources=[AMIid['ImageId']],
	    		Tags=[
	    			{'Key': 'DeleteOn_Yearly', 'Value': delete_fmt},
	    			{'Key': 'Instance', 'Value': instance['InstanceId']},
			    ]
            )