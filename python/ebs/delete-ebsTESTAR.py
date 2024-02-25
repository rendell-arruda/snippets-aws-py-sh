import boto3

def excluir_lista_volumes_ebs(volume_ids):
    # Crie um cliente EC2
    ec2 = boto3.client('ec2')

    volumes_nao_excluidos = []

    for volume_id in volume_ids:
        try:
            # Excluir o volume EBS
            ec2.delete_volume(VolumeId=volume_id)
            print(f"Volume EBS {volume_id} excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir o volume EBS {volume_id}: {str(e)}")
            # Adicionar o volume à lista de volumes que não puderam ser excluídos
            volumes_nao_excluidos.append(volume_id)

    return volumes_nao_excluidos

# Lista de IDs de volumes EBS que você deseja excluir
volumes_para_excluir = ['vol-00000000000000000', 
                        'vol-0000000000000000c']

# Chamando a função para excluir a lista de volumes EBS
volumes_nao_excluidos = excluir_lista_volumes_ebs(volumes_para_excluir)

# Imprimir os volumes que não puderam ser excluídos
print("\nVolumes EBS não excluídos:")
print("\n".join(volumes_nao_excluidos))
