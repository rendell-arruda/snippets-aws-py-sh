import boto3
from datetime import datetime, timedelta


def listar_snapshots_com_paginacao(regions):
    # Itera sobre as regiões
    for region in regions:
        print(f"### {region} ###")

        # Cria uma sessão e um cliente para cada região
        session = boto3.Session(profile_name="default")
        ec2 = session.client("ec2", region_name=region)

        # Utiliza o paginador para listar todos os snapshots
        paginator = ec2.get_paginator("describe_snapshots")
        snapshots_iterator = paginator.paginate(OwnerIds=["self"])

        # Itera sobre as páginas
        for page in snapshots_iterator:
            snapshots = page["Snapshots"]

            # TEST
            for snapshot in snapshots:
                print(snapshot["Description"])
            # TEST

            # Lista para armazenar os snapshots que podem ou não ser excluídos
            snapshots_linked_ami = []
            snapshots_can_delete = []

            # Percore a lista de snapshots
            # for snapshot in snapshots:
            #     # Lista AMIs para verificar se há snapshots em uso por elas.
            #     response = ec2.describe_images()


# Lista de regiões
regions = ["us-east-1", "sa-east-1"]

# Chama a função para listar snapshots com paginação
listar_snapshots_com_paginacao(regions)
