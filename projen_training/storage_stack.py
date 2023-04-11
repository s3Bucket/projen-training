import os
from aws_cdk import Stack, aws_s3 as s3, aws_glue as glue
from constructs import Construct


class StorageStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    raw_data_bucket = s3.Bucket(self, "Isa-Raw-Data")
    delta_data_bucket = s3.Bucket(self, "Isa-Delta-Data")
    
    glue.CfnJob(self, "PythonShellJob", 
                name="python-shell-job", 
                command=glue.CfnJob.JobCommandProperty(
                  name='pythonshell',
                  python_version='3.9'
                ),
                role="role.arn",
                glue_version='3.0',
                timeout=3
    )
    