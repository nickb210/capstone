#!/bin/bash


echo "\ndocker-compose -f deploy/docker-compose.yml run --rm terraform init"
echo "********************************************************************"
docker-compose -f deploy/docker-compose.yml run --rm terraform init

echo "\ndocker-compose -f deploy/docker-compose.yml run --rm terraform plan"
echo "********************************************************************"
docker-compose -f deploy/docker-compose.yml run --rm terraform plan
