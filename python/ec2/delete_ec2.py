import boto3

session = boto3.Session(profile_name="default")

def deletar_lista_instancias_ec2(instance_ids):
    # Crie um cliente EC2
    ec2 = session.client('ec2')

    try:
        # Termine (delete) as instâncias EC2
        response = ec2.terminate_instances(InstanceIds=instance_ids)
        
        # Verifique o estado das instâncias terminadas
        for instance in response['TerminatingInstances']:
            print(f"Instância {instance['InstanceId']} - Estado: {instance['CurrentState']['Name']}")
        
        print("Instâncias EC2 terminadas com sucesso.")
    except Exception as e:
        print(f"Erro ao terminar instâncias EC2 {instance_ids}:\n {str(e)}")

# Lista de IDs de instâncias EC2 que você deseja excluir
instancia_ids_para_excluir = ["i-0230a7aaaaaaaaaa"]

# Chamando a função com a lista de IDs de instâncias EC2
deletar_lista_instancias_ec2(instancia_ids_para_excluir)
