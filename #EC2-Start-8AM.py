#EC2-Start-8AM


import boto3
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g.; 'us-east-1'
region = 'ap-south-1'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['i-029b638910270c808']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))





    {
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "CloudFormation template for EventBridge rule 'EC2-Start-8AM'",
  "Resources": {
    "EventRule0": {
      "Type": "AWS::Events::Rule",
      "Properties": {
        "Description": "EC2 instances starts at everyday 8 AM IST",
        "EventBusName": "default",
        "Name": "EC2-Start-8AM",
        "ScheduleExpression": "cron(30 02 * * ? *)",
        "State": "ENABLED",
        "Targets": [{
          "Id": "Id7342170634255",
          "Arn": "arn:aws:lambda:ap-south-1:437097720063:function:EC2-Start-8AM"
        }]
      }
    }
  }
}