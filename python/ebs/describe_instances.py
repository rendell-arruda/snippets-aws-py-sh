import boto3
ec2 = boto3.client('ec2')
# descrever as instancias de uma conta
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
      print(f"ID da Instância: {instance['InstanceId']}")
      
