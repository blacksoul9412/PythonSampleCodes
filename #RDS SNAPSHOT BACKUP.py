#RDS SNAPSHOT BACKUP

import botocore  
import datetime  
import re  
import logging
import boto3
 
region='ap-south-1'    
instances = ['cholams-pre-prod-db-cluster']
 
print('Loading function')
 
def lambda_handler(event, context):  
     source = boto3.client('rds', region_name=region)
     for instance in instances:
         try:
             #timestamp1 = '{%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
             timestamp1 = str(datetime.datetime.now().strftime('%Y-%m-%d'))
             snapshot = "{0}-{1}".format(instance,timestamp1)
             response = source.create_db_snapshot(DBSnapshotIdentifier=snapshot, DBInstanceIdentifier=instance)
             print(response)
         except botocore.exceptions.ClientError as e:
             raise Exception("Could not create snapshot: %s" % e)