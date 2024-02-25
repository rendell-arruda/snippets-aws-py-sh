#!bin/bash

#listar tg
aws elbv2 describe-target-groups --output text

#listar tg e suas infos
aws elbv2 describe-target-groups --query 'TargetGroups[*].[TargetGroupArn, TargetGroupName, VpcId, Protocol, Port]' --output text | sed 's/\t/","/g; s/.*/"&",/; $s/,$//' > tg-list.txt

