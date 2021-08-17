#!/bin/bash

echo "printenv"
echo "==========================="
printenv

echo "echo PATH"
echo "=========================="
echo $PATH


#docker-compose -f deploy/docker-compose.yml run --rm terraform plan
