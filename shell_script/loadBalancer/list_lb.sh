#!/bin/bash

# Nome do arquivo de saída
output_file="load_balancers.txt"

# Obtém uma lista de todos os Load Balancers na conta
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName, LoadBalancerArn]' --output text > $output_file

# Informa que o script foi concluído e onde os resultados foram salvos
echo "Listagem de Load Balancers concluída. Resultados salvos em: $output_file"
