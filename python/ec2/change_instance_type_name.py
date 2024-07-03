import boto3

# Configurar a sessão do boto3
session = boto3.Session(profile_name="default")

# Inicializar o cliente EC2
ec2_client = session.client("ec2")


# Função para obter o ID da instância a partir do nome
def get_instance_id_by_name(instance_name):
    try:
        response = ec2_client.describe_instances(
            Filters=[{"Name": "tag:Name", "Values": [instance_name]}]
        )
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                return instance["InstanceId"]
        return None
    except Exception as e:
        print(f"Erro ao obter o ID da instância pelo nome {instance_name}:\n{str(e)}")
        return None


# Função para mudar o tipo de instância
def change_instance_type(instance_name, new_instance_type):
    try:
        instance_id = get_instance_id_by_name(instance_name)
        if instance_id is None:
            print(f"Instância com nome {instance_name} não encontrada.")
            return

        # Parar a instância
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Parando a instância {instance_id} ({instance_name})...")

        # Esperar até que a instância esteja parada
        waiter = ec2_client.get_waiter("instance_stopped")
        waiter.wait(InstanceIds=[instance_id])
        print(f"A instância {instance_id} ({instance_name}) está parada.")

        # Mudar o tipo da instância
        ec2_client.modify_instance_attribute(
            InstanceId=instance_id, InstanceType={"Value": new_instance_type}
        )
        print(
            f"Tipo da instância {instance_id} ({instance_name}) alterado para {new_instance_type}."
        )

        # Iniciar a instância
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Iniciando a instância {instance_id} ({instance_name})...")

        # Esperar até que a instância esteja em execução
        waiter = ec2_client.get_waiter("instance_running")
        waiter.wait(InstanceIds=[instance_id])
        print(f"A instância {instance_id} ({instance_name}) está em execução.")

        print(f"Tipo da instância {instance_name} alterado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao alterar o tipo da instância {instance_name}: {e}")


# Lista de nomes de instâncias e novo tipo de instância
instance_names = [
    "panvishp",
    "ec2_change_type",
]  # Substitua pelos nomes das suas instâncias
new_instance_type = "t2.micro"  # Substitua pelo novo tipo de instância desejado

# Loop para mudar o tipo de todas as instâncias na lista
for name in instance_names:
    change_instance_type(name, new_instance_type)
