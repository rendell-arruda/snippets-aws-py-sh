import boto3

# Configurar a sessão do boto3
session = boto3.Session(
    profile_name="default",
    region_name="us-east-1",  # Substitua pela região desejada
)

# Inicializar o cliente EC2
ec2_client = session.client("ec2")


# Função para mudar o tipo de instância
def change_instance_type(instance_id, new_instance_type):
    try:
        # Parar a instância
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Parando a instância {instance_id}...")

        # # Esperar até que a instância esteja parada
        waiter_stopped = ec2_client.get_waiter("instance_stopped")
        waiter_stopped.wait(InstanceIds=[instance_id])
        print(f"A instância {instance_id} está parada.")

        # Mudar o tipo da instância
        ec2_client.modify_instance_attribute(
            InstanceId=instance_id, InstanceType={"Value": new_instance_type}
        )
        print(f"Tipo da instância {instance_id} alterado para {new_instance_type}.")

        # Iniciar a instância
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Iniciando a instância {instance_id}...")

        # Esperar até que a instância esteja em execução
        waiter_started = ec2_client.get_waiter("instance_running")
        waiter_started.wait(InstanceIds=[instance_id])
        print(f"A instância {instance_id} está em execução.")

        print("Tipo da instância alterado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao alterar o tipo da instância: {e}")


# Exemplo de uso
instance_id = "i-063555cf5fdccbb69"  # Substitua pelo ID da sua instância
new_instance_type = "t2.micro"  # Substitua pelo novo tipo de instância desejado

change_instance_type(instance_id, new_instance_type)
