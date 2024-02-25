#!/bin/bash

# Arquivo que contém os ARNs dos instances RDS
arquivo_arns_instance_rds="./arns_instances_rds.txt"
conta="222222222222"
prefix_arn=("arn:aws:rds:us-east-1:$conta:instance:")

# Verifica se o arquivo de ARNs dos instances RDS existe
if [ -f "$arquivo_arns_instance_rds" ]; then

    # Variável para armazenar IDs dos instances RDS que não puderam ser tagueados
    instances_rds_falha=""

    # Loop para adicionar as tags aos instances RDS
    while IFS= read -r arn_instance_rds || [[ -n $arn_instance_rds ]]; do
        output=$(aws rds add-tags-to-resource --resource-name "${prefix_arn}${arn_instance_rds}" --tags Key=key1,Value=valeu1 Key=key2,Value=valeu2 2>&1)

        if [[ $? -eq 0 ]]; then
            echo "Tags adicionadas ao instance RDS (ARN): $arn_instance_rds"
        else
            echo "Falha ao adicionar tags ao instance RDS (ARN): $arn_instance_rds: $output"
            instances_rds_falha+=" $arn_instance_rds"
        fi
    done < "$arquivo_arns_instance_rds"

else
    echo "O arquivo $arquivo_arns_instance_rds não foi encontrado."
fi

# Mostra os ARNs dos instances RDS que não puderam ser tagueados
if [ -n "$instances_rds_falha" ]; then
    echo " "
    echo "Resultado:"
    echo "instances RDS (ARN) que não conseguiram ser tagueados: $instances_rds_falha"
else
    echo "Todos os instances RDS foram tagueados com sucesso."
fi
