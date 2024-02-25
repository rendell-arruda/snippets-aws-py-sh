#!/bin/bash

# Arquivo que contém os IDs das chaves KMS
arquivo_ids="./ids_kms.txt"

# Verifica se o arquivo de IDs existe
if [ -f "$arquivo_ids" ]; then

    # Variável para armazenar IDs das chaves KMS que não puderam ser tagueadas
    chaves_falha=""

    # Loop para adicionar as tags às chaves KMS
    while IFS= read -r id_kms || [[ -n $id_kms ]]; do
        output=$(aws kms tag-resource --resource-id "$id_kms" --tags TagKey1=Valor1 TagKey2=Valor2 2>&1)

        if [[ $? -eq 0 ]]; then
            echo "Tags adicionadas à chave KMS $id_kms"
        else
            echo "Falha ao adicionar tags à chave KMS $id_kms: $output"
            chaves_falha+=" $id_kms"
        fi
    done < "$arquivo_ids"

else
    echo "O arquivo $arquivo_ids não foi encontrado."
fi

# Mostra os IDs das chaves KMS que não puderam ser tagueadas
if [ -n "$chaves_falha" ]; then
    echo " "
    echo "Resultado:"
    echo "Chaves KMS que não conseguiram ser tagueadas: $chaves_falha"
else
    echo "Todas as chaves KMS foram tagueadas com sucesso."
fi
