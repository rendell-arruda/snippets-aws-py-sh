import boto3

# Configuração do cliente DocumentDB
session = boto3.Session(
    profile_name="default"
)  # Inicializa a sessão do boto3 com o perfil 'default'
client_docdb = session.client(
    "docdb", region_name="us-east-1"
)  # Cria um cliente para o serviço DocumentDB na região us-east-1


# Função para adicionar tags a um recurso DocumentDB (cluster ou instância)
def adicionar_tags_a_recurso(recurso_arn, tags):
    """
    Adiciona as tags especificadas a um recurso DocumentDB (cluster ou instância).

    Args:
        recurso_arn (str): O ARN (Amazon Resource Name) do recurso DocumentDB.
        tags (list): Uma lista de dicionários contendo as tags a serem adicionadas ao recurso.

    Returns:
        None
    """
    client_docdb.add_tags_to_resource(
        ResourceName=recurso_arn,  # ARN do recurso DocumentDB
        Tags=tags,  # Tags a serem adicionadas
    )
    print(
        f"Tags adicionadas ao recurso {recurso_arn}"
    )  # Imprime uma mensagem informando que as tags foram adicionadas ao recurso


# Função para listar todos os clusters DocumentDB na conta e adicionar tags a cada um deles
def adicionar_tags_a_clusters(tags):
    """
    Lista todos os clusters DocumentDB na conta e adiciona as tags especificadas a cada um deles e às suas instâncias associadas.

    Args:
        tags (list): Uma lista de dicionários contendo as tags a serem adicionadas a cada cluster e suas instâncias associadas.

    Returns:
        None
    """
    response = (
        client_docdb.describe_db_clusters()
    )  # Obtém informações sobre todos os clusters DocumentDB na conta
    clusters = response["DBClusters"]  # Obtém a lista de clusters

    # Itera sobre cada cluster
    for cluster in clusters:
        cluster_arn = cluster["DBClusterArn"]  # Obtém o ARN do cluster
        print(cluster_arn)  # Imprime o ARN do cluster
        adicionar_tags_a_recurso(cluster_arn, tags)  # Adiciona as tags ao cluster

        # Obtém as instâncias associadas ao cluster
        response_instances = client_docdb.describe_db_instances(
            Filters=[
                {"Name": "db-cluster-id", "Values": [cluster["DBClusterIdentifier"]]}
            ]
        )
        instances = response_instances[
            "DBInstances"
        ]  # Obtém a lista de instâncias associadas ao cluster

        # Itera sobre cada instância associada ao cluster
        for instance in instances:
            instance_arn = instance["DBInstanceArn"]  # Obtém o ARN da instância
            adicionar_tags_a_recurso(instance_arn, tags)  # Adiciona as tags à instância


# Tags que você deseja adicionar a todos os clusters e instâncias
tags_para_adicionar = [
    {"Key": "AutoStart", "Value": "true"},
    {"Key": "AutoStop", "Value": "true"},
]

# Adicionar tags a todos os clusters e instâncias
adicionar_tags_a_clusters(tags_para_adicionar)

print("Tags adicionadas aos clusters e instâncias DocumentDB.")
