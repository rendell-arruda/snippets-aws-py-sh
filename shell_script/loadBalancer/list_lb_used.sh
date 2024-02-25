#!/bin/bash

# Nome do arquivo de saída
output_file="load_balancers_em_uso.txt"

# Obtém uma lista de todos os Load Balancers na conta
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName, LoadBalancerArn]' --output text | while read -r lb_name lb_arn; do
    # Obtém as instâncias associadas ao Load Balancer
    instances=$(aws elbv2 describe-target-health --target-group-arn $(aws elbv2 describe-listeners --load-balancer-arn $lb_arn --query 'Listeners[*].DefaultActions[*].TargetGroupArn' --output text) --query 'TargetHealthDescriptions[*].Target.Id' --output text)

    # Verifica se há instâncias associadas
    if [ -n "$instances" ]; then
        # Imprime o nome e ARN do Load Balancer em uso e redireciona para o arquivo
        echo "Load Balancer em uso: $lb_name ($lb_arn)" >> "$output_file"
    fi
done

# Informa que o script foi concluído e onde os resultados foram salvos
echo "Listagem de Load Balancers em uso concluída. Resultados salvos em: $output_file"
