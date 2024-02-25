import boto3

# function para excluir
def delete_load_balancer(load_balancer_name,falhas):
    # cliente de comunicacao com o servico elbv2 para ter acesso aos metodos dele
    elbv2 = boto3.client('elbv2')

    try:
        elbv2.delete_load_balancer(LoadBalancerArn=load_balancer_name)
        print(f"Load balancer {load_balancer_name} excluído com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir load balancer {load_balancer_name}: {str(e)}")
        falhas.append(load_balancer_name)

# lista dos lb que deseja excluir
load_balancer_names = ['arn:aws:elasticloadbalancing:us-east-1:conta:loadbalancer/nomeelb', 'arn:aws:elasticloadbalancing:us-east-1:conta:loadbalancer/nomeelb2' ]
#lista dos itens não excluidos
load_balancers_nao_excluidos = []

#chamada da function passando um lb
for lb in load_balancer_names:
    delete_load_balancer(lb, load_balancers_nao_excluidos)

# print dos lb que nao puderam ser excluidos
print("\nLoad balancers não excluídos:")
print("\n".join(load_balancers_nao_excluidos))