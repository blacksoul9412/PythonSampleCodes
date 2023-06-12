#prod-rds-weekly-backup

import boto3
import datetime
def lambda_handler(event, context):
    print("Connecting to RDS")
    rds_client = boto3.client('rds')
    db_instance_info = rds_client.describe_db_instances()
    
    for each_db in db_instance_info['DBInstances']:
        response = rds_client.list_tags_for_resource(ResourceName=each_db['DBInstanceArn'])
        taglist = response['TagList']
        for tag in taglist:
            if tag['Key'] == 'Snapshotweekly' and tag['Value'] == 'yes':
                rds_client.create_db_snapshot(
                DBInstanceIdentifier=each_db['DBInstanceIdentifier'],
                DBSnapshotIdentifier=each_db['DBInstanceIdentifier']+"-"+"Weekly"+str(datetime.datetime.now().strftime("%Y-%m-%d")),
        Tags=[
            {
                'Key': 'RDSweesnapshot',
                'Value': '11PM'
            },
        ]
    )
