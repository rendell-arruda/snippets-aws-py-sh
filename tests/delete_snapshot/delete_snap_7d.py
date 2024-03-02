import boto3
from datetime import datetime, timedelta

regions = ["us-east-1", "sa-east-1"]


def listar_snapshots_com_paginacao(regions):
    # percorre as regioes
    for region in regions:
        print(f"### {region} ###")

        # para cada regiao abrir uma session e um client
        session = boto3.Session(profile_name="default")
        ec2 = session.client("ec2", region_name=region)

        # Lista todos os snapshots
        # snapshots = ec2.describe_snapshots(OwnerIds=["self"])["Snapshots"]

        # iniciar a paginacao
        paginator = ec2.get_paginator("describe_snapshots")
        snapshot_iterator = paginator.paginate(OwnerIds=["self"])

        # Iterar sobre as paginas
        for page in snapshot_iterator:
            snapshots = page["Snapshots"]

        # TEST
        for snapshot in snapshots:
            print(snapshot["Description"])
        # TEST

        # lista para armazenar os snapshot que podem ou nao ser excluidos
        snapshots_linked_ami = []
        snapshots_can_delete = []

        # percorrer a lista de snapshots
        # for snapshot in snapshots:
        #     # lista amis para verificar se há snapshot em uso por elas.
        #     response = ec2.describe_images()


# Lista de regiões
regions = ["us-east-1", "sa-east-1"]

# Chama a função para listar snapshots com paginação
listar_snapshots_com_paginacao(regions)
