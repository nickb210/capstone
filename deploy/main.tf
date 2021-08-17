terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  #version = "~> 2.54.0"
}

# get resource that give us region
data "aws_region" "current" {}
