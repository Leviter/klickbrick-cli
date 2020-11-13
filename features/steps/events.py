import sys
import subprocess
import inspect
import os.path

import unittest

from behave import given, when, then
from klickbrick_cli import klickbrick
from server import app


@given("a running server to receive events")
def run_the_connexion_server(context):
    # app.run(True)
    # app.run(False)
    context.tester = app.app.test_client()
    context.tester.post("/event")


@when("running the application with the help command")
def run_the_app_with_the_help_command(context):
    context.output = klickbrick.run(["onboard", "--checklist"])


@then("the event contains the command")
def check_server_output_for_command(context):
    # output = context.server_output.getvalue().strip()
    # assert "help" in output
    return


@then("the event contains the parameters")
def check_server_output_for_command_parameters(context):
    # output = context.server_output.getvalue().strip()
    # assert "onboard" in output
    return


@then("the event contains the OS")
def check_server_output_for_os(context):
    # output = context.server_output.getvalue().strip()
    # assert "macOS" in output
    return
