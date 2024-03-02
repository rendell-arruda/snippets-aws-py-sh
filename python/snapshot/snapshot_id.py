import boto3
import csv

def lambda_handler(event, context):
    # Lista de regiões
    regions = ['us-east-1', 'sa-east-1']
    
    # Função para excluir snapshots
    def delete_snapshot(snapshot_id, falhas):
        excluido = False
        
        for region in regions:
            print(f"### {snapshot_id} ###")
            print(f"### {region} ###")
            
            try:
                # Configuração da sessão e criação do cliente EC2
                session = boto3.Session(profile_name='default', region_name=region)
                client = session.client('ec2')
                
                # Exclusão do snapshot
                client.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Volume EBS {snapshot_id} excluído com sucesso")
                excluido = True
                break
                
            except Exception as e:
                # Tratamento de exceções em caso de erro na exclusão
                print(f"Erro ao excluir snapshot {snapshot_id} - ERROR: {str(e)}")
                continue
        
        # Adiciona o ID do snapshot à lista de falhas, se não foi excluído
        print("\n")
        if not excluido and snapshot_id not in falhas:
            falhas.append(snapshot_id)

    # Ler o arquivo externo com os IDs dos snapshots
    with open('snapshot_list.csv', 'r') as file:
        reader = csv.reader(file)
        snapshot_ids = [row[0] for row in reader]

    snapshot_nao_excluidos = []

    # Chamar a função delete_snapshot para cada ID de snapshot
    for snapshot_id in snapshot_ids:
        delete_snapshot(snapshot_id, snapshot_nao_excluidos)

    # Imprimir os snapshots não excluídos
    print("\nSnapshots não excluídos:")
    print("\n".join(snapshot_nao_excluidos))

# Este bloco permite que o código seja testado localmente, mas não é executado na AWS Lambda.
if __name__ == '__main__':
    lambda_handler(None, None)
