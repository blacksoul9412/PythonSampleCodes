#CIS-EvaluateVpcDefaultSecurityGroups



import boto3
import json
def lambda_handler(event, context):
  is_compliant = True
  invoking_event = json.loads(event['invokingEvent'])
  annotation = ''
  security_group_id = invoking_event['configurationItem']['resourceId']
  # Get security groups details
  security_group = boto3.client('ec2').describe_security_groups(GroupIds=[security_group_id])['SecurityGroups']
  # evaluate the default security groups compliance
  if security_group[0]['GroupName'] == 'default':
    if security_group[0]['IpPermissions']:
      annotation = annotation + 'The security group has ingress rules in place.'
      is_compliant = False
    if security_group[0]['IpPermissionsEgress']:
      annotation = annotation + ' The security group has egress rules in place.'
      is_compliant = False
    evaluations = [
      {
        'ComplianceResourceType': invoking_event['configurationItem']['resourceType'],
        'ComplianceResourceId': security_group_id,
        'ComplianceType': 'COMPLIANT' if is_compliant else 'NON_COMPLIANT',
        'OrderingTimestamp': invoking_event['configurationItem']['configurationItemCaptureTime']
      }
    ]
    if annotation: evaluations[0]['Annotation'] = annotation
    response = boto3.client('config').put_evaluations(
      Evaluations = evaluations,
      ResultToken = event['resultToken']
    )
