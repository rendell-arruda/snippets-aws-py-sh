import boto3

def encontrar_instancia_por_volume(volume_id):
    # Crie um cliente EC2
    ec2 = boto3.client('ec2')

    try:
        # Obtenha informações sobre o volume EBS
        response = ec2.describe_volumes(VolumeIds=[volume_id])

        if 'Volumes' in response and len(response['Volumes']) > 0:
            instance_id = response['Volumes'][0]['Attachments'][0]['InstanceId']
            print(f"O volume EBS {volume_id} está atualmente anexado à instância {instance_id}")
            return instance_id
        else:
            print(f"O volume EBS {volume_id} não está atualmente anexado a nenhuma instância.")
            return None

    except Exception as e:
        print(f"Erro ao buscar informações do volume EBS {volume_id}: {str(e)}")
        return None

def desanexar_lista_volumes_ebs(volume_ids):
    for volume_id in volume_ids:
        # Encontrar a instância associada ao volume
        instance_id = encontrar_instancia_por_volume(volume_id)

        # Se a instância for encontrada, tentar desanexar o volume
        if instance_id:
            try:
                # Crie um cliente EC2
                ec2 = boto3.client('ec2')

                # Desanexar o volume EBS da instância EC2
                response = ec2.detach_volume(VolumeId=volume_id)

                # Verifique o estado da operação de desanexação
                if 'VolumeId' in response:
                    print(f"Volume EBS {volume_id} desanexado com sucesso da instância {instance_id}")
                else:
                    print(f"Falha ao desanexar o volume EBS {volume_id}")

            except Exception as e:
                print(f"Erro ao desanexar o volume EBS {volume_id}: {str(e)}")

# Lista de IDs de volumes EBS que você deseja desanexar
volumes_para_desanexar = ['vol-id']

# Chamando a função para desanexar a lista de volumes EBS
desanexar_lista_volumes_ebs(volumes_para_desanexar)
