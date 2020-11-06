import sys

from behave import when, then
from klickbrick_cli import klickbrick


@when("passed the help parameter")
def run_application_with_help_parameter(context):
    context.output = klickbrick.run(["help"])


@when("passed the help parameter with onboard")
def run_application_with_help_and_onboard_parameter(context):
    print("Starting")
    context.output = klickbrick.run(["help", "onboard"])
    print("Done")


@then("information is shown about various commands")
def check_for_help_on_commands(context):
    output = sys.stdout.getvalue().strip()
    assert "{onboard}" in output


@then("information is shown about the onboard parameter")
def check_output_contains_help_on_onboard(context):
    sys.__stdout__.write(sys.stdout.getvalue().strip())
    output = sys.stdout.getvalue().strip()
    assert "onboard" in output
    assert "--checklist" in output
