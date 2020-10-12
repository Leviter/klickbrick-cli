import sys
import io


def before_all(context):
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock


def after_all(context):
    sys.stdout = context.real_stdout
