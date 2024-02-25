#!/bin/bash

# Arquivo que contém os ARNs dos clusters RDS
arquivo_arns_cluster_rds="./arns_clusters_rds.txt"
conta="000000000000"

prefix_arn=("arn:aws:rds:us-east-1:$conta:cluster:")

# Verifica se o arquivo de ARNs dos clusters RDS existe
if [ -f "$arquivo_arns_cluster_rds" ]; then

    # Variável para armazenar IDs dos clusters RDS que não puderam ser tagueados
    clusters_rds_falha=""

    # Loop para adicionar as tags aos clusters RDS
    while IFS= read -r arn_cluster_rds || [[ -n $arn_cluster_rds ]]; do
        output=$(aws rds add-tags-to-resource --resource-name "${prefix_arn}${arn_cluster_rds}" --tags Key=key1,Value=valeu1 Key=key2,Value=valeu2 2>&1)

        if [[ $? -eq 0 ]]; then
            echo "Tags adicionadas ao cluster RDS (ARN): $arn_cluster_rds"
        else
            echo "Falha ao adicionar tags ao cluster RDS (ARN): $arn_cluster_rds: $output"
            clusters_rds_falha+=" $arn_cluster_rds"
        fi
    done < "$arquivo_arns_cluster_rds"

else
    echo "O arquivo $arquivo_arns_cluster_rds não foi encontrado."
fi

# Mostra os ARNs dos clusters RDS que não puderam ser tagueados
if [ -n "$clusters_rds_falha" ]; then
    echo " "
    echo "Resultado:"
    echo "Clusters RDS (ARN) que não conseguiram ser tagueados: $clusters_rds_falha"
else
    echo "Todos os clusters RDS foram tagueados com sucesso."
fi
