import boto3
import csv

session = boto3.Session(profile_name="default")

# Crie um cliente EC2
ec2_client = session.client("ec2")

# Descreva instâncias EC2
response = ec2_client.describe_instances()

# Lista para armazenar detalhes das instâncias
instances_details = []

# especificar o nome do arquivo de saida
output_file = "ec2_details.json"

# Iterar sobre todas as respostas [Reservations]
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        # Pegar os detalhes da instância
        instance_id = instance["InstanceId"]
        instance_state = instance["State"]["Name"]

        instances_details.append(
            {"Instance Id": instance_id, "Instance State": instance_state}
        )

# Iterar sobre todas as reservas e instâncias
# for reservation in response["Reservations"]:
#     print(reservation)
# for instance in reservation["Instances"]:
#     # Pegar o ID da instância
#     instance_id = instance["InstanceId"]

#     # Pegar o tipo da instância
#     instance_type = instance["InstanceType"]

#     print(f"Instance ID: {instance_id}")
#     print(f"Instance Type: {instance_type}")

#     instances_details.append(
#         {"Instance ID": instance_id, "Instance Type": instance_type}
#     )

# Adicionar os detalhes da instância na lista
# instances_details.append(
#     {
#         "Instance ID": instance_id,
#         "Instance Type": instance_type,
#     }
# )
# print(instances_details)

## Salvar a saída no arquivo txt
with open(output_file, "w") as f:
    f.write(str(instances_details))
