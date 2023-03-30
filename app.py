from constructs import Construct
from cdk8s import App, Chart


class MyChart(Chart):
  def __init__(self, scope: Construct, id:str):
    super().__init__(scope, id)


app = App()
MyChart(app, "${project.name}")

app.synth()