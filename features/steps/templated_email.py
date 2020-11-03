import sys

from behave import when, then
from klickbrick_cli import klickbrick


@when('passed the it-request parameter with firstname "{firstname}" and lastname "{lastname}"')
def run_application_with_it_request_and_firs_and_last_name(context, firstname, lastname):
    context.output = klickbrick.run(["onboard", "--it-request", "--first-name", firstname, "--last-name", lastname])


@then('name "{name}" is in the email')
def check_the_output_for_name(context, name):
    output = sys.stdout.getvalue().strip()
    assert name in output
