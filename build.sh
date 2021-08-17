#!/bin/bash

docker-compose -f deploy/docker-compose.yml run --rm terraform plan
