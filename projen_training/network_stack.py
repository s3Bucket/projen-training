import os
from aws_cdk import Stack, Tags, aws_ec2
from constructs import Construct


class NetworkStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    vpc = aws_ec2.Vpc(self, "TheVPC", cidr="10.0.0.0/16")
    Tags.of(scope).add("Owner", "bu-aws")