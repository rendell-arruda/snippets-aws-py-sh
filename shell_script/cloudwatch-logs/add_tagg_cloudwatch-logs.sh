#!/bin/bash

# Arquivo que contém os nomes dos grupos de logs do CloudWatch
arquivo_grupos_logs="./nomes_grupos_logs.txt"

# Verifica se o arquivo de nomes de grupos de logs existe
if [ -f "$arquivo_grupos_logs" ]; then

    # Variável para armazenar nomes dos grupos de logs que não puderam ser tagueados
    grupos_logs_falha=""

    # Loop para adicionar as tags aos grupos de logs do CloudWatch
    while IFS= read -r nome_grupo_logs || [[ -n $nome_grupo_logs ]]; do
        output=$(aws logs tag-log-group --log-group-name "$nome_grupo_logs" --tags Key=Key1,Value=value1 Key=Key2,Value=value2 2>&1)

        if [[ $? -eq 0 ]]; then
            echo "Tags adicionadas ao grupo de logs do CloudWatch: $nome_grupo_logs"
        else
            echo "Falha ao adicionar tags ao grupo de logs do CloudWatch: $nome_grupo_logs: $output"
            grupos_logs_falha+=" $nome_grupo_logs"
        fi
    done < "$arquivo_grupos_logs"

else
    echo "O arquivo $arquivo_grupos_logs não foi encontrado."
fi

# Mostra os nomes dos grupos de logs do CloudWatch que não puderam ser tagueados
if [ -n "$grupos_logs_falha" ]; then
    echo " "
    echo "Resultado:"
    echo "Grupos de logs do CloudWatch que não conseguiram ser tagueados: $grupos_logs_falha"
else
    echo "Todos os grupos de logs do CloudWatch foram tagueados com sucesso."
fi
