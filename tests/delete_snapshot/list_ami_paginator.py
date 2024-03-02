import boto3


def listar_amis_com_paginacao():
    # Crie um cliente EC2
    ec2_client = boto3.client("ec2")

    # Defina os filtros que deseja aplicar
    filters = [
        # {"Name": "owner-id", "Values": ["self"]}
    ]

    # Use o paginador para lidar com a paginação
    paginator = ec2_client.get_paginator("describe_images")

    # Ajuste o tamanho da página conforme necessário
    page_iterator = paginator.paginate(
        Filters=filters, Owners=["self"], PaginationConfig={"PageSize": 1000}
    )

    # Itere sobre as páginas
    for page in page_iterator:
        # Itere sobre as AMIs na página atual
        for ami in page["Images"]:
            # Faça algo com a AMI, como imprimir o ID
            # print(ami["ImageId"])
            ami_block = ami["BlockDeviceMappings"]
            print(ami_block[0]["Ebs"]["SnapshotId"])


# Chame a função para listar todas as AMIs próprias da conta com paginacao
listar_amis_com_paginacao()
