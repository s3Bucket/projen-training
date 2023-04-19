import re
import unittest
from aws_cdk import App
from aws_cdk.assertions import Template
from aws_cdk import aws_s3 as s3

from projen_training.storage_stack import StorageStack

class StorageStackTest(unittest.TestCase):
  
  def setUp(self):
    app = App()
    self.stack = StorageStack(app, "storage-stack-test")
    self.template = Template.from_stack(self.stack)
  
  def test_there_are_two_buckets(self):
    self.template.resource_count_is("AWS::S3::Bucket", 2)    
  
  def test_describing_isa_raw_data_bucket(self):
    with self.subTest('template contains bucket name with resource name prefix'):
      resource_name = "IsaRawData"
      assert(resource_name in self.assertBucketPrefixExists(resource_name))
    
    with self.subTest('describing_resource'):
      self.template.has_resource(
        "AWS::S3::Bucket",
          {
            "DeletionPolicy": "Delete"
          }
      )
    
    with self.subTest('describing_resource properties'):
      self.template.has_resource_properties(
        "AWS::S3::Bucket",
        {
          "VersioningConfiguration": { "Status": "Enabled" }
        }
      )
      
  def test_describing_isa_delta_data_bucket(self):
    with self.subTest('describing_resource'):
      self.template.has_resource(
        "AWS::S3::Bucket",
        {
          "DeletionPolicy": "Retain"
        }
      )
      
  def assertBucketPrefixExists(self, prefix):
      s3Prefixes = [] 
      for key in self.template.find_resources("AWS::S3::Bucket"):
        res = re.findall(fr"^{prefix}", key)
        s3Prefixes.append(res)
      return [prefix for sublist in s3Prefixes for prefix in sublist]
