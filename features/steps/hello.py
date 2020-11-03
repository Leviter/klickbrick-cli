from behave import when, then
from klickbrick_cli import hello


@when(u"I start the program without any parameters")
def run_application_without_parameters(context):
    context.output = hello.get_greeting("")


@when(u"I start the program with the hello parameter")
def run_application_with_hello_parameter(context):
    context.output = hello.get_greeting(["hello"])


@when(u"I start the program with the hello parameter and a name parameter having the value Marcel")
def run_application_with_name(context):
    context.output = hello.get_greeting(["hello", "--name", "Marcel"])


@then(u'it prints "{text}"')
def check_output(context, text):
    assert context.output == text
