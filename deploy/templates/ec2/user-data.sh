#!/bin/bash
sudo yum update -y

# install & start docker 
sudo amazon-linux-extras install -y docker
sudo systemctl enable docker.service
sudo systemctl start docker.service

# add our EC2 user to the Docker group
sudo usermod -aG docker ec2-user

 aws ecr get-login --no-include-email --region us-east-1
$(aws ecr get-login --no-include-email --region us-east-1)

# pull docker image from Docker Hub
sudo docker pull nickb09/capstone:latest

# run our docker image
sudo docker run -p 80:80 nickb09/capstone:latest 
