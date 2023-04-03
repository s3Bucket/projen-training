import os
from aws_cdk import Stack, Tags, aws_ec2 as ec2
from constructs import Construct


class NetworkStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    vpc = ec2.Vpc(self, "CdkClusterVPC", ip_addresses=ec2.IpAddresses.cidr("192.168.0.0/16"), max_azs=1,  subnet_configuration=[
        ec2.SubnetConfiguration(
            cidr_mask=24,
            name="NATnet",
            subnet_type=ec2.SubnetType.PUBLIC
        ),
        ec2.SubnetConfiguration(
            cidr_mask=24,
            name="node1",
            subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
        )
    ])
    Tags.of(scope).add("Owner", "bu-aws")
    