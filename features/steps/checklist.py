from behave import *
from klickbrick_cli import klickbrick

import os.path

CHECKLIST_FILE = "checklist.md"

use_step_matcher("re")


@given("the command")
def step_impl(context):
    return


@given("markdown file is absent")
def step_impl(context):
    if os.path.exists(CHECKLIST_FILE):
        os.remove("checklist.md")
    assert not os.path.isfile(CHECKLIST_FILE)


@when("passed the checklist parameter")
def step_impl(context):
    context.output = klickbrick.run(['onboard', '--checklist'])


@then("a markdown file is created")
def step_impl(context):
    print(context.output)
    assert os.path.isfile(CHECKLIST_FILE)
