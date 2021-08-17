# Provide VPC resource
resource "aws_vpc" "main" {
  cidr_block           = "10.1.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "My-VPC"
  }
}

# Resource to create a VPC internet gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}

# =================================================
# Define and Configure Network
# =================================================
# Provide VPC subnet
resource "aws_subnet" "dmz" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.1.1.0/24"
  #map_public_ip_on_launch = true
  availability_zone = "us-east-1a"
}

# Create VPC routing table
resource "aws_route_table" "public_subnet" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
}

# Create an association between our route table and our subnet
resource "aws_route_table_association" "public_subnet" {
  subnet_id      = aws_subnet.dmz.id
  route_table_id = aws_route_table.public_subnet.id
}

