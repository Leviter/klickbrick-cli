from unittest import TestCase

from klickbrick_cli import klickbrick


class Test(TestCase):
    def test_email_template_replace(self):
        template = "This should replace both {{firstname}} and {{lastname}}"
        firstname = "Marcel"
        lastname = "van den Brink"
        expected = "This should replace both Marcel and van den Brink"
        self.assertEqual(klickbrick.email_template_replace(template, firstname, lastname), expected)
