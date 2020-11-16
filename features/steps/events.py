import sys

from behave import given, when, then
from io import StringIO
from klickbrick_cli import klickbrick


@given("a non-running server to receive events")
def do_nothing(context):
    sys.stdout = StringIO()


@when("running the application with the help command")
def run_the_app_with_the_help_command(context):
    context.output = klickbrick.run(["onboard", "--checklist"])


@then("a timout is logged")
def check_for_retries(context):
    output = sys.stdout.getvalue().strip()
    assert "Max retries exceeded" in output
