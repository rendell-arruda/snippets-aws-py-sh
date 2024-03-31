import boto3

# Configuração do cliente DocumentDB
session = boto3.Session(profile_name="default")
client_docdb = session.client("docdb", region_name="us-east-1")


# Função para adicionar tags a um cluster DocumentDB
def add_tag(cluster_arn, tags):

    client_docdb.add_tags_to_resource(
        ResourceName=cluster_arn,
        Tags=tags,
    )
    print(f"Tags adicionadas ao cluster {cluster_arn}")


# Função para listar todos os clusters DocumentDB na conta e adicionar tags a cada um deles
def adicionar_tags_a_clusters(tags):
    response = client_docdb.describe_db_clusters()
    clusters = response["DBClusters"]

    for cluster in clusters:
        cluster_arn = cluster["DBClusterArn"]
        print(cluster_arn)
        add_tag(cluster_arn, tags)


# Tags que você deseja adicionar a todos os clusters
tags_para_adicionar = [
    {"Key": "AutoStart", "Value": "true"},
    {"Key": "AutoStop", "Value": "true"},
]

# Adicionar tags a todos os clusters
adicionar_tags_a_clusters(tags_para_adicionar)

print("Tags adicionadas aos clusters DocumentDB.")
