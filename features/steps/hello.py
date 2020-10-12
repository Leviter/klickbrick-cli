from behave import when
from behave import then
from klickbrick_cli import hello


@when(u'I start the program')
def step_impl(context):
    hello.main()


@then(u'it prints "{text}"')
def step_impl(context, text):
    output = context.stdout_mock.getvalue()
    assert output == "hello world\n"
