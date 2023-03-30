from projen.python import PythonProject

project = PythonProject(
    author_email="cschmidt@evoila.de",
    author_name="Colin Schmidt",
    module_name="projen_training",
    name="projen-training",
    version="0.1.0",
)

project.synth()