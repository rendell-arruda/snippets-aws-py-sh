import boto3

def excluir_volume_ebs(volume_id, falhas):
    ec2 = boto3.client('ec2')

    try:
        ec2.delete_volume(VolumeId=volume_id)
        print(f"Volume EBS {volume_id} excluído com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir volume EBS {volume_id}: {str(e)}")
        falhas.append(volume_id)

# Lista de IDs dos volumes EBS que você deseja excluir
volume_ids = ['vol-00000000000000000', 
              'vol-00000000000000007']
volumes_nao_excluidos = []

for volume_id in volume_ids:excluir_volume_ebs(volume_id, volumes_nao_excluidos)

print("\nVolumes EBS não excluídos:")
print("\n".join(volumes_nao_excluidos))
