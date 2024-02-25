import boto3

def delete_lista_target_group(target_group_arns):
    #crie um client elbv2
    elbv2 = boto3.client('elbv2')
    for target_group_arn in target_group_arns:
        try:
            #excluir um tg
            elbv2.delete_target_group(TargetGroupArn=target_group_arn)
            print(f"Target group {target_group_arn} excluido com sucesso.")
        
        except Exception as e:
            print(f"Erro ao deletar o Target group {target_group_arn}:\n {str(e)}.")

target_group_arns = ["arn:aws:elasticloadbalancing:us-east-1:conta:targetgroup/name",
"arn:aws:elasticloadbalancing:us-east-1:conta:targetgroup/name2"
]

delete_lista_target_group(target_group_arns)