import boto3
ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId="ami-0005e0cfe09ccaaaa",
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName="key_name"
)[0]
