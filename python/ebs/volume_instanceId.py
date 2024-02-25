import boto3
#   saber qual instanceId que o volume esta atachado
ec2 = boto3.resource('ec2')
volumeId = 'vol-id'
response = ec2.Volume(volumeId).attachments[0]['InstanceId']
print(f'{response}')

