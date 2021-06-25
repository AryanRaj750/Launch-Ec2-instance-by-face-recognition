provider "aws" {
       region = "ap-south-1"
       profile = "terraform"
}
resource "aws_instance" "SPec2" {
  ami           = "ami-011c99152163a87ae"
  instance_type = "t3.micro"
  key_name = "key Name"

  tags = {
    Name = "SP ec2"
  }
}

resource "aws_ebs_volume" "SPtask6" {
  availability_zone = aws_instance.SPec2.availability_zone
  size              = 2

  tags = {
    Name = "Sp ebs volume"
  }
}
resource "aws_volume_attachment" "EBSattach" {
  device_name = "/dev/sdb"
  volume_id   = aws_ebs_volume.SPtask6.id
  instance_id = aws_instance.SPec2.id
}
