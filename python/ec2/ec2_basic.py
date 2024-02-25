import boto3

# cria uma instancia ec2
ec2_client = boto3.resource('ec2')
instance = ec2_client.create_instances(
        ImageId='ami-12345678',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )[0]

# Inicia a instancia
instance.start()

# Para a instance
instance.stop()

# Termina a instancia
instance.terminate()

