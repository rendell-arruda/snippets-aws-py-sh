#!/bin/bash

# Array com os IDs das VPCs que você deseja etiquetar
ids_vpcs=("vpc-02409877622222222" 
          "vpc-0e222233442222222")

# Loop para adicionar as tags às VPCs
for id_vpc in "${ids_vpcs[@]}"; do
    output=$(aws ec2 create-tags --resources "$id_vpc" --tags Key=key1,Value=value1 Key=key2,Value=value2 2>&1)

    if [[ $? -eq 0 ]]; then
        echo "Tags adicionadas à VPC $id_vpc"
    else
        echo "Falha ao adicionar tags à VPC $id_vpc: $output"
    fi
done