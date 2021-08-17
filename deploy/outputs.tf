output "instance_aws_eip" {
  value = aws_eip.public_subnet.public_ip
}


output "public_dns" {
    description = "List of public DNS names assigned to the instances"
    value = aws_instance.Capstone.public_dns
}