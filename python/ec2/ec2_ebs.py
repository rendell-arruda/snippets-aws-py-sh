import boto3
import csv

# Define a lista de regiões para buscar as instâncias EC2
regions = ["us-east-1"]


def lambda_handler(event, context):
    # Abre ou cria o arquivo CSV para escrita
    with open("./python/ec2/ec2_volumes.csv", mode="w", newline="") as csv_file:
        # Define os nomes das colunas do CSV
        fieldnames = ["InstanceId", "VolumeId"]
        # Cria um escritor de CSV com os nomes das colunas definidos
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # Escreve o cabeçalho no arquivo CSV
        writer.writeheader()

        # Itera sobre cada região especificada
        for region in regions:
            # Cria uma sessão boto3 usando o perfil padrão
            session = boto3.Session(profile_name="default")
            # Cria um cliente EC2 para a região atual
            ec2_client = session.client("ec2", region_name=region)

            # Descreve todas as instâncias EC2 na região
            instances = ec2_client.describe_instances()
            for reservation in instances["Reservations"]:
                for instance in reservation["Instances"]:
                    # Obtém o ID da instância
                    instanceId = instance["InstanceId"]

                    # Descreve os volumes anexados à instância
                    volumes = ec2_client.describe_volumes(
                        Filters=[
                            {"Name": "attachment.instance-id", "Values": [instanceId]}
                        ]
                    )

                    for volume in volumes["Volumes"]:
                        # Obtém o ID do volume
                        volumeId = volume["VolumeId"]
                        # Imprime o ID do volume e o ID da instância no console
                        print(f" {volumeId} : {instanceId}")

                        # Escreve o ID da instância e o ID do volume no arquivo CSV
                        writer.writerow(
                            {"InstanceId": instanceId, "VolumeId": volumeId}
                        )


# Ponto de entrada do script quando executado diretamente
if __name__ == "__main__":
    lambda_handler({}, {})
