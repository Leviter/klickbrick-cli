import sys

from behave import when, then
from klickbrick_cli import klickbrick


@when("passed the help parameter")
def step_impl(context):
    context.output = klickbrick.run(["help"])


@then("information is shown about various commands")
def check_for_help_on_commands(context):
    output = sys.stdout.getvalue().strip()
    assert "{onboard}" in output


@when("passed the help parameter and onboard")
def run_application_with_help_and_onboard_parameter(context):
    context.output = klickbrick.run(["help", "onboard"])


@then("information is shown about the onboard parameter")
def check_output_contains_help_on_onboard(context):
    output = sys.stdout.getvalue().strip()
    assert "onboard" in output
    assert "--checklist" in output
