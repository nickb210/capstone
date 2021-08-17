#!/bin/bash

#echo "printenv"
#echo "==========================="
#printenv

#echo "echo PATH"
#echo "=========================="
#echo $PATH


echo "docker-compose -f deploy/docker-compose.yml run --rm terraform init"
echo "********************************************************************"
docker-compose -f deploy/docker-compose.yml run --rm terraform init

echo "docker-compose -f deploy/docker-compose.yml run --rm terraform plan"
echo "********************************************************************"
docker-compose -f deploy/docker-compose.yml run --rm terraform plan
