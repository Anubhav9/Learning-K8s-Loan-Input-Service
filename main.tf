provider "aws"{
    region="ap-northeast-1"
}
resource "aws_instance" "loan-input-service"{
    ami="ami-0a290015b99140cd1"
    instance_type="t2.micro"
    security_groups = [ aws_security_group.loan-input-service-security-group ]
    user_data = file("docker-instructions-ec2.sh")
    tags={
        Name="loan-input-service-box"
    }

}
resource "aws_security_group" "loan-input-service-security-group"{
    name="Loan Input Service Security Group"
    description="Security Group for Loan Input Service"
    ingress=[{
        description="HTTP Ingress Port"
        from_port=80
        to_port=80
        protocol="tcp"
        cidr_blocks=["0.0.0.0/0"]
    },
    {
        description="HTTPS Ingress Port"
        from_port=443
        to_port=443
        protocol="tcp"
        cidr_blocks=["0.0.0.0/0"]
    },
    {
        description="Custom TCP Port to access application"
        from_port=2809
        to_port=2809
        protocol="tcp"
        cidr_blocks=["0.0.0.0/0"]
    }]
    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
    tags={
        Name="loan-input-service-security-group"
    }
}
