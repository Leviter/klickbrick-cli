from behave import *
from klickbrick_cli import klickbrick

use_step_matcher("re")


@given("the command")
def step_impl(context):
    return


@when("passed the checklist parameter")
def step_impl(context):
    context.output = klickbrick.run(['onboard', '--checklist'])


@then("a markdown file is created")
def step_impl(context):
    print(context.output)
    assert context.output != ''
