import unittest
import pytest
from aws_cdk import App
from aws_cdk.assertions import Template

from projen_training.storage_stack import StorageStack

class StorageStackTest(unittest.TestCase):
  
  def test_my(self):
    app = App()
    stack = StorageStack(app, "storage-stack-test")
    template = Template.from_stack(stack)
    
    with self.subTest('There are two buckets'):
      template.resource_count_is("AWS::S3::Bucket", 2)
      
    with self.subTest('describing Isa-Raw-Data Bucket'):
      template.has_resource(
            "AWS::S3::Bucket",
            {
                "DeletionPolicy": "Delete"
            }
      )
      
      template.has_resource_properties(
        "AWS::S3::Bucket",
        {
            "VersioningConfiguration": { "Status": "Enabled" }
        }
      )
      
    with self.subTest('describing Isa-Delta-Data Bucket'):
      template.has_resource(
            "AWS::S3::Bucket",
            {
                "DeletionPolicy": "Retain"
            }
      )
      


