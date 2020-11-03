import sys

from behave import when, then
from klickbrick_cli import klickbrick


@when('passed the install parameter and the tool "{name}"')
def run_application_with_install_parameter(context, name):
    context.output = klickbrick.run(["onboard", "--install", name])


@then('"{name}" is installed')
def check_output_for_install(context, name):
    output = sys.stdout.getvalue().strip()
    assert "Installing" in output
    assert name in output
