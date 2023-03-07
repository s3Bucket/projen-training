from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="cschmidt@evoila.de",
    author_name="Colin Schmidt",
    cdk_version="2.1.0",
    module_name="projen_training",
    name="projen-training",
    version="0.1.0",
)

project.synth()