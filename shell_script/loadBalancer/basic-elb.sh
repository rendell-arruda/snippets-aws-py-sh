#!bin/bash

#Listar loadbalancer v1
aws elb describe-load-balancers --query "LoadBalancers[*].LoadBalancerArn" --output text

#Listar loadbalancer v2
aws elbv2 describe-load-balancers 

#listar loadbalancer pelo arn separa-los por virgula e aspas                                Para que a saída ja venha com aspas e separado por virgula
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].LoadBalancerArn' --output text | sed 's/\t/","/g; s/.*/"&",/; $s/,$//' > elbv2-arns.csv

#listar tg
aws elbv2 describe-target-groups --output text

#listar tg e suas infos
aws elbv2 describe-target-groups --query 'TargetGroups[*].[TargetGroupArn, TargetGroupName, VpcId, Protocol, Port]' --output text | sed 's/\t/","/g; s/.*/"&",/; $s/,$//' > tg-list.txt

