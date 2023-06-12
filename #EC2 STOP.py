#EC2 STOP

import boto3
region = 'ap-south-1'
instances = ['i-054dac888936edcdc']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))