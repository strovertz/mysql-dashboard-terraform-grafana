variable "grafana-sg" {
  type    = string
  default = "grafana-internal-sg"
}

variable "aws_profile" {
  type    = string
  default = "universidade"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "tags" {
  type = map(string)
  default = {
    Terraform   = "true"
    Environment = "prd"
  }
}

variable "user_data_path" {
  type    = string
  default = "/internal-scripts/userdata.sh"
}

variable "subnet-1a" {
  default = "subnet-051cde3327cd6d841"
}

variable "vpc_default" {
  default = "vpc-09e888a015bbebfdb"
}

variable "aws_secgrp_port" {

  type = number

  description = "Portas to|from"

  default = 80

}

variable "cidr_blocks" {

  type = string

  description = "when cidr_blocks equals '0.0.0.0/0'"

  default = "0.0.0.0/0"
}

variable "cidr_blocks_ssh" {

  type = string

  description = "when cidr_blocks is defined by usr'"

  default = "0.0.0.0/0"
}

variable "tcp" {

  type = string

  description = "tcp"

  default = "tcp"
}

variable "instance_ami" {

  type = string

  description = "AMI do ubuntu"

  default = "ami-052efd3df9dad4825"
}

variable "instance_type" {

  type = string

  description = "Instance type"

  default = "t3.micro"
}

variable "instance_tags" {

  type = map(string)

  description = "tags"

  default = {

    Name = "Servidor-grafana"

    Project = "teste"

  }
}

variable "PRIVATE_KEY_PATH" {
  default = "gleison"
}

variable "PUBLIC_KEY_PATH" {
  default = "gleison.pub"
}

variable "EC2_USER" {
  default = "ubuntu"
}

/*variable "ec2" {
  description = "The attribute of EC2 information"
  type = object({
    name              = "ppshein"
    os_type           = "ubuntu"
    instance_type     = "t2.micro"
    volume_size       = 20
    volume_type       = "gp3"
    availability_zone = "us-east-1a"
  })
}*/
variable "os_type" {
  type    = string
  default = "ubuntu"

}