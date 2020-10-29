from unittest import TestCase

from klickbrick_cli import klickbrick


class Test(TestCase):
    def test_get_hello_greeting(self):
        print(klickbrick.run(['onboard']))
        self.assertEqual(klickbrick.run(['hello']), "hello world")

    def test_get_named_greeting(self):
        self.assertEqual(klickbrick.run(['hello', '--name', 'Charlie']), "hello Charlie")

    def test_get_empty_name_greeting(self):
        self.assertEqual(klickbrick.run(['hello', '--name', '']), "hello ")

