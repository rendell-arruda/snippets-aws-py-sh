#!/bin/bash

# Nome do arquivo de saída
output_file="load_balancers_sem_uso.txt"

# Obtém uma lista de todos os Load Balancers na conta
aws elbv2 describe-load-balancers --query 'LoadBalancers[?length(ListenerDescriptions)==`0`].LoadBalancerArn' --output text | while read -r lb_arn; do
    # Verifica se não há instâncias associadas
    if [ -z "$(aws elbv2 describe-target-health --target-group-arns $(aws elbv2 describe-listeners --load-balancer-arn $lb_arn --query 'Listeners[*].DefaultActions[*].TargetGroupArn' --output text) --query 'TargetHealthDescriptions[*].Target.Id' --output text)" ]; then
        # Imprime o ARN do Load Balancer que não está em uso e redireciona para o arquivo
        echo "Load Balancer não em uso: $lb_arn" >> $output_file
    fi
done

# Informa que o script foi concluído e onde os resultados foram salvos
echo "Verificação concluída. Resultados salvos em: $output_file"
