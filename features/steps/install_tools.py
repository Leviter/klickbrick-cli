import sys

from behave import when, then
from klickbrick_cli import klickbrick


@when('passed the install parameter and the tool "{name}"')
def step_impl(context, name):
    context.output = klickbrick.run(['onboard', '--install', name])


@then('"{name}" is installed')
def step_impl(context, name):
    output = sys.stdout.getvalue().strip()
    assert "Installing" in output
    assert name in output
