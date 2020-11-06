import sys
import os

from behave import when, then
from klickbrick_cli import klickbrick


@when("passed the init parameter and a project {name} and directory {path}")
def run_application_with_init_parameters(context, name, path):
    context.output = klickbrick.run(["init", "--name", name, "--path", path])


@then("the directory {path} for the project is created")
def check_directory_for_project_is_created(context, path):
    assert os.path.isdir(path)
    context.projectPath = path


@then("correctly initialised")
def check_project_initialisation(context):
    sys.__stdout__.write(sys.stdout.getvalue().strip())
    assert os.path.isdir(context.projectPath + os.path.sep + ".git")
    assert os.path.isfile(context.projectPath + os.sep + "CONTRIBUTING.md")
    assert os.path.isfile(context.projectPath + os.sep + "README.md")
