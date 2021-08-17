#!/bin/bash

#echo "printenv"
#echo "==========================="
#printenv

#echo "echo PATH"
#echo "=========================="
#echo $PATH

ls

echo "\naws-vault list"
echo "********************************************************************"
aws-vault list

echo "\naws-vault exec nick.brell -d 12h"
echo "********************************************************************"
aws-vault exec nick.brell -d 12h
aws-vault list
#echo $AWS_VAULT


echo "\ndocker-compose -f deploy/docker-compose.yml run --rm terraform init"
echo "********************************************************************"
docker-compose -f deploy/docker-compose.yml run --rm terraform init

echo "\ndocker-compose -f deploy/docker-compose.yml run --rm terraform plan"
echo "********************************************************************"
docker-compose -f deploy/docker-compose.yml run --rm terraform plan
