import boto3

# Configuração do cliente DocumentDB
session = boto3.Session(profile_name="default")
client_docdb = session.client("docdb", region_name="us-east-1")


# Função para adicionar tags a um cluster DocumentDB
def taguear_cluster(recurso_arn, tags):
    """Args:
        recurso_arn (str): O ARN (Amazon Resource Name) do cluster DocumentDB.
        tags (list): Uma lista de dicionários contendo as tags a serem adicionadas ao cluster.

    Returns:
        None
    """
    client_docdb.add_tags_to_resource(
        ResourceName=recurso_arn,  # ARN do recurso DocumentDB
        Tags=tags,  # Tags a serem adicionadas
    )
    print(f"Tags adicionadas ao cluster {recurso_arn}")


# Função para listar todos os clusters DocumentDB na conta e adicionar tags a cada um deles
def adicionar_tags_a_clusters(tags):
    """
    Args:
        tags (list): Uma lista de dicionários contendo as tags a serem adicionadas a cada cluster.
    """
    response = client_docdb.describe_db_clusters()
    clusters = response["DBClusters"]

    # Itera sobre cada cluster
    for cluster in clusters:
        cluster_arn = cluster["DBClusterArn"]
        taguear_cluster(cluster_arn, tags)


# Tags que você deseja adicionar a todos os clusters
tags_para_adicionar = [
    {"Key": "AutoStart", "Value": "true"},
    {"Key": "AutoStop", "Value": "true"},
]

# Adicionar tags a todos os clusters
adicionar_tags_a_clusters(tags_para_adicionar)

print("Tags adicionadas aos clusters DocumentDB.")
