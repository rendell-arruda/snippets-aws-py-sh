import boto3


def listar_amis_sem_paginacao():
    # Crie um cliente EC2
    ec2_client = boto3.client("ec2")

    # Defina os filtros que deseja aplicar
    # filters = [Owners=['self']]

    # Faça uma chamada única para listar todas as AMIs sem usar paginador
    response = ec2_client.describe_images(Owners=["self"])

    # Itere sobre as AMIs na resposta
    for ami in response["Images"]:
        # Faça algo com a AMI, como imprimir o ID
        print(f"ID da AMI: {ami['ImageId']}")


# Chame a função para listar todas as AMIs próprias da conta sem paginar
listar_amis_sem_paginacao()
