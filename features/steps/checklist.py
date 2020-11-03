from behave import given, when, then
from klickbrick_cli import klickbrick

import os.path

CHECKLIST_FILE = "checklist.md"


@given("the command")
def step_impl(context):
    return


@given("markdown file is absent")
def check_for_absent_file(context):
    if os.path.exists(CHECKLIST_FILE):
        os.remove("checklist.md")
    assert not os.path.isfile(CHECKLIST_FILE)


@when("passed the checklist parameter")
def run_klickbrick_application(context):
    context.output = klickbrick.run(["onboard", "--checklist"])


@then("a markdown file is created")
def check_for_file(context):
    print(context.output)
    assert os.path.isfile(CHECKLIST_FILE)
