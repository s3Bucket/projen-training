import pytest
from aws_cdk import App
from aws_cdk.assertions import Template

from projen_training.storage_stack import StorageStack

@pytest.fixture(scope='module')
def template():
  app = App()
  stack = StorageStack(app, "storage-stack-test")
  template = Template.from_stack(stack)
  yield template

def test_two_buckets_found(template):
  template.resource_count_is("AWS::S3::Bucket", 2)
  
def test_glue_job_found(template):
  template.resource_count_is("AWS::Glue::Job", 1)  
