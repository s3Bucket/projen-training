from projen.awscdk import AwsCdkPythonApp
import projen.github as github
import projen.github.workflows as workflows

project = AwsCdkPythonApp(
    author_email="cschmidt@evoila.de",
    author_name="Colin Schmidt",
    cdk_version="2.1.0",
    module_name="projen_training",
    name="projen-training",
    version="0.1.0",
    deps=["pytest"],
    poetry=True,
)

workflow = project.github.add_workflow(name="reusable-worflows")
workflow.on(push={"branches":["*"]})
workflow.add_jobs(
    {
        "test-YAML": {
            "name": "Check YAML streams",
            "uses": "evoila/GitHub-Actions/.github/workflows/reusable-YAML.yaml@v0.6.0",
            "permissions": workflows.JobPermissions(),
            "with": {
                "python-version-file": ".python-version"
            }
        },
        "test-Markdown": {
            "name": "Check Markdown documents",
            "uses": "evoila/GitHub-Actions/.github/workflows/reusable-Markdown.yaml@v0.6.0",
            "permissions": workflows.JobPermissions(),
            "with": {
                "node-version-file": ".nvmrc"
            }
        }
    }
)


project.synth()