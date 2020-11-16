from unittest import TestCase
from server import events_server


class Test(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = events_server.create_app()
        cls.client = cls.app.test_client()
        cls.client.testing = True

    def test_post_event(self):
        response = self.client.post('/event', json={"command":"testcmd", "parameters":"testparam", "os":"macOS", "python_version:":"3.9"})
        print(response.status_code)
        assert response.status_code == 202
