output "instance_aws_eip" {
  value = aws_eip.public_subnet.public_ip
}

output "instance_public_dns" {
    description = "Public DNS name assigned to the EC2 instance"
    value = aws_instance.Capstone.instance_public_dns
}

output "public_dns" {
    description = "List of public DNS names assigned to the instances"
    value = aws_instance.Capstone.public_dns
}