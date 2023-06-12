#EC2-Stop-9PM

import boto3
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., 'us-east-1'
region = 'ap-south-1'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['i-09b4431e859367f1a','i-0d835e980cb69fb05','i-094ce09f20d3bc741']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))