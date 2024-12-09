import boto3
from datetime import datetime, timedelta, timezone
session = boto3.Session(profile_name='sandbox')

import boto3
import csv
from datetime import datetime, timezone

# Função para verificar se uma role não foi usada nos últimos 90 dias
def role_unused_for_90_days(last_used_date):
    if not last_used_date:
        # Caso a role nunca tenha sido usada
        return True
    now = datetime.now(timezone.utc)  # Torna 'now' compatível com o timezone da AWS
    return (now - last_used_date).days > 90

def list_unused_iam_roles(output_csv='unused_roles.csv'):
    iam_client = session    .client('iam')
    unused_roles = []

    try:
        # Paginação para obter todas as roles
        paginator = iam_client.get_paginator('list_roles')
        for page in paginator.paginate():
            for role in page['Roles']:
                role_name = role['RoleName']
                print(f"Verificando role: {role_name}")

                # Obter detalhes de acesso da role
                response = iam_client.get_role(RoleName=role_name)
                last_used_date = response['Role'].get('RoleLastUsed', {}).get('LastUsedDate')

                # Verifica se a role não foi usada nos últimos 90 dias
                if role_unused_for_90_days(last_used_date):
                    unused_roles.append({
                        'RoleName': role_name,
                        'LastUsedDate': last_used_date.isoformat() if last_used_date else 'Never'
                    })

        # Salva as roles não usadas no arquivo CSV
        with open(output_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['RoleName', 'LastUsedDate'])
            writer.writeheader()
            writer.writerows(unused_roles)

        print(f"Roles que não foram usadas nos últimos 90 dias foram salvas em: {output_csv}")

    except Exception as e:
        print(f"Erro ao listar as IAM roles: {e}")

if __name__ == "__main__":
    list_unused_iam_roles()