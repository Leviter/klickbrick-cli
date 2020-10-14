from behave import when, then
from klickbrick_cli import hello


@when(u'I start the program without any parameters')
def step_impl(context):
    context.output = hello.get_greeting("")


@when(u'I start the program with the hello parameter')
def step_impl(context):
    context.output = hello.get_greeting(["hello"])


@when(u'I start the program with the hello parameter and a name parameter having the value Marcel')
def step_impl(context):
    context.output = hello.get_greeting(["hello", "--name", "Marcel"])


@then(u'it prints "{text}"')
def step_impl(context, text):
    assert context.output == text
