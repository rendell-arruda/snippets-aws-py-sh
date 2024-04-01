import boto3

# Configuração do cliente DocumentDB
session = boto3.Session(profile_name="default")
client_docdb = session.client("docdb", region_name="us-east-1")


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
        ResourceName=recurso_arn,
        Tags=tags,
    )
    print(f"Tags adicionadas ao recurso {recurso_arn}")


# Função para adicionar tags ao cluster e suas instâncias associadas
def adicionar_tags_ao_cluster_e_instancias(arn_cluster, tags):
    """
    Adiciona as tags especificadas ao cluster DocumentDB e suas instâncias associadas.

    Args:
        arn_cluster (str): O ARN do cluster DocumentDB.
        tags (list): Uma lista de dicionários contendo as tags a serem adicionadas ao cluster e suas instâncias.

    Returns:
        None
    """
    # Adiciona as tags ao cluster
    adicionar_tags_a_recurso(arn_cluster, tags)

    # Obtém o identificador do cluster a partir do ARN
    cluster_identifier = arn_cluster.split(":")[-1]

    # Obtém as instâncias associadas ao cluster
    response_instances = client_docdb.describe_db_instances(
        Filters=[{"Name": "db-cluster-id", "Values": [cluster_identifier]}]
    )
    instances = response_instances["DBInstances"]

    # Adiciona as tags a cada instância associada ao cluster
    for instance in instances:
        instance_arn = instance["DBInstanceArn"]
        adicionar_tags_a_recurso(instance_arn, tags)

    print("Tags adicionadas ao cluster e suas instâncias DocumentDB.")


# Função para solicitar o ARN do cluster na linha de comando
def solicitar_arn_cluster():
    """
    Solicita ao usuário que insira o ARN do cluster DocumentDB na linha de comando.

    Returns:
        str: O ARN do cluster DocumentDB fornecido pelo usuário.
    """
    arn_cluster = input("Digite o ARN do cluster DocumentDB: ")
    return arn_cluster


# Tags que você deseja adicionar ao cluster e suas instâncias
tags_para_adicionar = [
    {"Key": "AutoStart", "Value": "false"},
    {"Key": "AutoStop", "Value": "false"},
]

# Solicita o ARN do cluster ao usuário
arn_cluster = solicitar_arn_cluster()

# Adicionar tags ao cluster e suas instâncias associadas
adicionar_tags_ao_cluster_e_instancias(arn_cluster, tags_para_adicionar)

print("Tags adicionadas ao cluster e suas instâncias DocumentDB.")
