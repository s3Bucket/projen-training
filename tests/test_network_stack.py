import pytest
from aws_cdk import App
from aws_cdk.assertions import Template

from projen_training.network_stack import NetworkStack

@pytest.fixture(scope='module')
def template():
  app = App()
  stack = NetworkStack(app, "network-stack-test")
  template = Template.from_stack(stack)
  yield template

def test_one_vpc_found(template):
  template.resource_count_is("AWS::EC2::VPC", 1)
  template.has_resource_properties(
        "AWS::EC2::VPC",
        {
            "CidrBlock": "10.0.0.0/16",
            "Tags" : [ {"Key": "Name", "Value": "network-stack-test/TheVPC"}, {"Key": "Owner", "Value":"bu-aws"} ]
        },
    )
