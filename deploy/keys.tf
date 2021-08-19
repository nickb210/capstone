# =================================================
# Define & Create SSH key for EC2 instance
# =================================================
resource "tls_private_key" "private_key" {
  algorithm = "RSA"
  rsa_bits = 4096
}

# create ssh key 
resource "aws_key_pair" "ssh_key" {
  key_name   = "ssh-key"
  public_key = tls_private_key.private_key.public_key_openssh

  # save public and private keys to local machine
  provisioner "local-exec" {
    command = "echo '${tls_private_key.private_key.public_key_openssh}' > ./ssh-key.rsa"
  }

  provisioner "local-exec" {
    command = "echo '${tls_private_key.private_key.private_key_pem}' > ./ssh-key.pem"
  }
}