from unittest import TestCase

from klickbrick_cli import hello


class Test(TestCase):
    def test_get_hello_greeting(self):
        self.assertEqual(hello.get_greeting(['hello']), "hello world")

    def test_get_named_greeting(self):
        self.assertEqual(hello.get_greeting(['hello', '--name', 'Charlie']), "hello Charlie")

    def test_get_empty_name_greeting(self):
        self.assertEqual(hello.get_greeting(['hello', '--name', '']), "hello ")

    def test_get_args_name(self):
        parsed_arguments = hello.get_args(['hello', '--name', 'Michael'])
        self.assertEqual(parsed_arguments.name, 'Michael')
