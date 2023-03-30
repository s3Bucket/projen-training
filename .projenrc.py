from projen.cdk8s import Cdk8sPythonApp

project = Cdk8sPythonApp(
    author_email="cschmidt@evoila.de",
    author_name="Colin Schmidt",
    cdk8s_version="2.3.33",
    module_name="projen_training",
    name="projen-training",
    version="0.1.0",
)

project.synth()