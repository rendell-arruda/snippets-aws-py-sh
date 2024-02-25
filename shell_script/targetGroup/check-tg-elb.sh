#!/bin/bash

# Lista de nomes de Load Balancers Classic
loadBalancerNames=("load-balancer-1" "load-balancer-2" "load-balancer-3")

# Loop sobre os nomes dos Load Balancers
for loadBalancerName in "${loadBalancerNames[@]}"; do
    # Obtém informações sobre o Load Balancer
    loadBalancerInfo=$(aws elb describe-load-balancers --load-balancer-name $loadBalancerName)

    # Verifica se o Load Balancer foi encontrado
    if [ $? -eq 0 ]; then
        # Extrai o ARN do Load Balancer
        loadBalancerArn=$(echo $loadBalancerInfo | jq -r '.LoadBalancerDescriptions[0].LoadBalancerArn')

        # Obtém informações sobre os Target Groups associados ao Load Balancer
        targetGroups=$(aws elbv2 describe-target-groups --load-balancer-arn $loadBalancerArn)

        # Verifica se há Target Groups associados
        if [ "$(echo $targetGroups | jq -r '.TargetGroups')" != "null" ]; then
            echo "Load Balancer '$loadBalancerName' está funcionando e tem Target Groups associado."
        else
            echo "Load Balancer '$loadBalancerName' está funcionando, mas não tem Target Groups associado."
        fi
    else
        echo "Erro ao obter informações sobre o Load Balancer '$loadBalancerName'."
    fi
done
#!/bin/bash

# Lista de nomes de Load Balancers Classic
loadBalancerNames=("load-balancer-1" "load-balancer-2" "load-balancer-3")

# Loop sobre os nomes dos Load Balancers
for loadBalancerName in "${loadBalancerNames[@]}"; do
    # Obtém informações sobre o Load Balancer
    loadBalancerInfo=$(aws elb describe-load-balancers --load-balancer-name $loadBalancerName)

    # Verifica se o Load Balancer foi encontrado
    if [ $? -eq 0 ]; then
        # Extrai o ARN do Load Balancer
        loadBalancerArn=$(echo $loadBalancerInfo | jq -r '.LoadBalancerDescriptions[0].LoadBalancerArn')

        # Obtém informações sobre os Target Groups associados ao Load Balancer
        targetGroups=$(aws elbv2 describe-target-groups --load-balancer-arn $loadBalancerArn)

        # Verifica se há Target Groups associados
        if [ "$(echo $targetGroups | jq -r '.TargetGroups')" != "null" ]; then
            echo "Load Balancer '$loadBalancerName' está funcionando e tem Target Groups associado."
        else
            echo "Load Balancer '$loadBalancerName' está funcionando, mas não tem Target Groups associado."
        fi
    else
        echo "Erro ao obter informações sobre o Load Balancer '$loadBalancerName'."
    fi
done
