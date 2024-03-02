# import boto3


# def listar_amis_sem_paginacao():
#     # Crie um cliente EC2
#     ec2_client = boto3.client("ec2")

#     # Defina os filtros que deseja aplicar
#     # filters = [Owners=['self']]

#     # Faça uma chamada única para listar todas as AMIs sem usar paginador
#     response = ec2_client.describe_images(Owners=["self"])

#     # Itere sobre as AMIs na resposta
#     for ami in response["Images"]:
#         # Faça algo com a AMI, como imprimir o ID
#         print(f"ID da AMI: {ami['ImageId']}")


# # Chame a função para listar todas as AMIs próprias da conta sem paginar
# listar_amis_sem_paginacao()


import boto3


def listar_amis_com_paginacao():
    # Crie um cliente EC2
    ec2_client = boto3.client("ec2")

    # Defina os filtros que deseja aplicar
    # filters = [{"Name": "owner-id", "Values": ["self"]}]

    # Use o paginador para lidar com a paginação
    paginator = ec2_client.get_paginator("describe_images")

    # Ajuste o tamanho da página conforme necessário
    page_iterator = paginator.paginate(
        Owners=["self"], PaginationConfig={"PageSize": 1000}
    )

    # Itere sobre as páginas
    for page in page_iterator:
        # Itere sobre as AMIs na página atual
        for ami in page["Images"]:
            # Faça algo com a AMI, como imprimir o ID
            print(f"ID da AMI: {ami['ImageId']}")


# Chame a função para listar todas as AMIs próprias da conta com paginacao
listar_amis_com_paginacao()
