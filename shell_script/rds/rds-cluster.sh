#!/bin/bash

# Array com os nomes das instâncias de banco de dados que você deseja etiquetar
# O rds usa o arn como name, louco ne?
nomes_rds=("database-1")
conta="xxxxxxxxx"
prefix_arn=("arn:aws:rds:us-east-1:$conta:cluster:")

# Loop para adicionar as tags às instâncias de banco de dados do RDS
for instancia_rds in "${nomes_rds[@]}"; do
    output=$(aws rds add-tags-to-resource --resource-name "${prefix_arn}${instancia_rds}" --tags Key=key1,Value=valeu1 Key=key2,Value=valeu2 2>&1)

    if [[ $? -eq 0 ]]; then
        echo "Tags adicionadas à instância de banco de dados RDS $instancia_rds"
    else
        echo "Falha ao adicionar tags à instância de banco de dados RDS $instancia_rds: $output"
    fi
done