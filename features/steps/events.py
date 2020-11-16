import sys
# import subprocess
# import inspect
# import os.path

# import unittest

from behave import given, when, then
from io import StringIO
from klickbrick_cli import klickbrick
# from server import events_server


# @given("a running server to receive events")
# def run_the_connexion_server(context):
#     app = events_server.create_app()
#     context.tester = app.test_client()
#     context.tester.testing = True


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


# @then("the event contains the command")
# def check_server_output_for_command(context):
#     # output = context.server_output.getvalue().strip()
#     # assert "help" in output
#     return
#
#
# @then("the event contains the parameters")
# def check_server_output_for_command_parameters(context):
#     # output = context.server_output.getvalue().strip()
#     # assert "onboard" in output
#     return
#
#
# @then("the event contains the OS")
# def check_server_output_for_os(context):
#     # output = context.server_output.getvalue().strip()
#     # assert "macOS" in output
#     return
