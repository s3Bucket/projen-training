import os
from aws_cdk import App, Environment
from projen_training.main import MyStack
from projen_training.network_stack import NetworkStack

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('CDK_DEFAULT_REGION')
)

app = App()
MyStack(app, "projen-training-dev", env=dev_env)
# MyStack(app, "projen-training-prod", env=prod_env)
NetworkStack(app, "projen-training-dev-network-stack", env=dev_env)

app.synth()