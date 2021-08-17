# =================================================
# Define EC2 Instance
# =================================================
data "aws_ami" "amazon_linux" {
  most_recent = true
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-2.0.20210617.0-x86_64-gp2"]
  }

  owners = ["amazon"]
}

# resource for IAM role
resource "aws_iam_role" "ec2" {
  name               = "aws-terraform-docker-role"
  assume_role_policy = file("./templates/ec2/instance-profile-policy.json")
}

resource "aws_iam_role_policy_attachment" "ec2_attatch_policy" {
  role       = aws_iam_role.ec2.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

# resource for our instance profile
resource "aws_iam_instance_profile" "ec2" {
  name = "aws-terraform-docker-ec2-instance-profile"
  role = aws_iam_role.ec2.name
}

resource "aws_instance" "Capstone" {
  /* "ami" and "isntance" are required for aws_instance resource */
  ami                  = data.aws_ami.amazon_linux.id
  instance_type        = "t2.micro"
  user_data            = file("./templates/ec2/user-data.sh")
  iam_instance_profile = aws_iam_instance_profile.ec2.name

  key_name  = aws_key_pair.ssh_key.key_name
  subnet_id = aws_subnet.dmz.id

  vpc_security_group_ids = [
    aws_security_group.base.id
  ]

  tags = {
    Name = "Capstone"
  }
}

resource "aws_security_group" "base" {
  name        = "SG-Capstone"
  description = "Control EC2 instances inbound and outbound access"
  vpc_id      = aws_vpc.main.id

  # Outbound HTTPS
  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound HTTP
  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow inbound SSH
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    #self        = false
  }

  # allow inbound HTTP request so Twilio app can work properly
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

}
# ====================================
# ELASTIC IP
# ====================================
# Resource for our Elastic IP
resource "aws_eip" "public_subnet" {
  # eip is a VPC
  vpc = true
}

# Resource to associate EIP's from AWS instances
resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.Capstone.id
  allocation_id = aws_eip.public_subnet.id
}

