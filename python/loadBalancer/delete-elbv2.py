import boto3

def excluir_elbv2(elbv2_arns):
    # Crie um cliente ELBV2
    elbv2 = boto3.client('elbv2')

    for elbv2_arn in elbv2_arns:
        try:
            # Exclua o ELB
            elbv2.delete_load_balancer(LoadBalancerArn=elbv2_arn)
            print(f"ELB {elbv2_arn} excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir ELB {elbv2_arn}:\n {str(e)}")

# Lista de ARNs dos ELBs que você deseja excluir
elbv2_arns = [ "arn:aws:elasticloadbalancing:us-east-1:conta:loadbalancer/name2",
            "arn:aws:elasticloadbalancing:us-east-1:conta:loadbalancer/name1"
]

# Chamando a função com a lista de ARNs
excluir_elbv2(elbv2_arns)
