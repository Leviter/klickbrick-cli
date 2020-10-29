import sys

from behave import when, then
from klickbrick_cli import klickbrick


@when('passed the it-request parameter with firstname "{firstname}" and lastname "{lastname}"')
def step_impl(context, firstname, lastname):
    context.output = klickbrick.run(['onboard', '--it-request', '--first-name', firstname, '--last-name', lastname])


@then('name "{name}" is in the email')
def step_impl(context, name):
    output = sys.stdout.getvalue().strip()
    assert name in output
