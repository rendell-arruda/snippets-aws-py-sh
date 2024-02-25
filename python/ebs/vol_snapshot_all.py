# Importa a biblioteca boto3, que é a biblioteca oficial da AWS para Python
import boto3
 
# Lista de regiões que serão verificadas
regions = ['us-east-1', 'sa-east-1']
 
# Função principal chamada pelo AWS Lambda
def lambda_handler(event, context):
    # Itera sobre as regiões especificadas
    for region in regions:
        # Imprime o nome da região sendo processada
        print(f'### {region} ###')
        
        # Cria uma sessão usando o profile 'default' e a região especificada
        session = boto3.Session(profile_name='default', region_name=region)
        
        # Cria um recurso EC2 usando a sessão configurada
        ec2 = session.resource('ec2')
        
        # Itera sobre todos os volumes EC2 na região
        for vol in ec2.volumes.all():
            # Obtém o ID do volume
            vol_id = vol.id
            
            # Imprime o ID do volume
            print(vol_id)
            
            # Itera sobre todos os snapshots associados ao volume
            for snap in vol.snapshots.all():
                # Imprime o ID do snapshot
                print(f"O snapshot: {snap.id} está associado ao volume {vol_id}")
                print(snap.tags)
                print('\n')
 
# Condição para verificar se o script está sendo executado diretamente (não como um módulo)
if __name__ == '__main__':
    # Chama a função lambda_handler passando dicionários vazios como argumentos
    lambda_handler({}, {})
