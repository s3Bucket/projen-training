import os
from aws_cdk import RemovalPolicy, Stack, aws_s3 as s3, aws_glue as glue
from constructs import Construct


class StorageStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    raw_data_bucket = s3.Bucket(self, "Isa-Raw-Data", removal_policy=RemovalPolicy.DESTROY, versioned=True)
    delta_data_bucket = s3.Bucket(self, "Isa-Delta-Data")
