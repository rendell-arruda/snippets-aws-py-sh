#!bin/bash

#list ec2
aws ec2 describe-instances --region us-east-1

#list ec2 filter name        regiao           filtrar saida  itera sobre as instancias e filtra id e tag Name      mostra apenas a 1* tag Name   retorna a saida num                
aws ec2 describe-instances --region us-east-1 --query "Reservations[*].Instances[*].[InstanceId,Tags[?Key=='Name'].Value|[O]]" --output text > ec2.txt

#list ec2 filter name        regiao           filtrar saida  itera sobre as instancias e filtra id e tag Name      mostra apenas a 1* tag Name   retorna a saida num                
aws ec2 describe-instances --region us-east-1 --query "Reservations[*].Instances[*].[InstanceId]" --output text | sed 's/\t/","/g; s/.*/"&",/; $s/,$//' > ec2Ids.txt

#listar instancias em running
aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query 'Reservations[*].Instances[*].[InstanceId]' --output text