import boto3

# Configuração do cliente DocumentDB
session = boto3.Session(profile_name="default")
client_docdb = session.client("docdb", region_name="us-east-1")


# Função para adicionar tags a um recurso DocumentDB (cluster)
def adicionar_tags_a_cluster(recurso_arn, tags):
    """
    Args:
        recurso_arn (str): O ARN (Amazon Resource Name) do cluster DocumentDB.
        tags (list): Uma lista de dicionários contendo as tags a serem adicionadas ao cluster.

    Returns:
        None
    """
    client_docdb.add_tags_to_resource(
        ResourceName=recurso_arn,
        Tags=tags,
    )
    print(f"Tags adicionadas ao cluster {recurso_arn}")


# Função para solicitar o ARN do cluster na linha de comando
def solicitar_arn_cluster():
    """
    Solicita ao usuário que insira o ARN do cluster DocumentDB na linha de comando.

    Returns:
        str: O ARN do cluster DocumentDB fornecido pelo usuário.
    """
    arn_cluster = input("Digite o ARN do cluster DocumentDB: ")
    return arn_cluster


# Tags que você deseja adicionar ao cluster
tags_para_adicionar = [
    {"Key": "AutoStart", "Value": "false"},
    {"Key": "AutoStop", "Value": "false"},
]

# Solicita o ARN do cluster ao usuário e armazena numa variavel
arn_cluster = solicitar_arn_cluster()

# Adicionar tags ao cluster DocumentDB
adicionar_tags_a_cluster(arn_cluster, tags_para_adicionar)

# se der certo
print("Tags adicionadas ao cluster DocumentDB.")
