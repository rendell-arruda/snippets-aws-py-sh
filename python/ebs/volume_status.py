import boto3
# cria um objeto de recursos EC2 usando boto3, usado para interagir com esses recursos
ec2 = boto3.resource('ec2')
volumeId = 'vol-id'
# variavel    resource.Metodo(parametro).propriedade[1*elemento da lista][chave]
response = ec2.Volume(volumeId).attachments[0]['State']
print(f'{response}')