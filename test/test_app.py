import unittest
from app import app

class TestMain(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "my-secret-key"
        app.config["ALLOWED_IPS"] = "127.0.0.1,192.168.1.1"
        self.app = app.test_client()

    def test_access_denied(self):
        response = self.app.get("/", headers={"X-Forwarded-For": "10.0.0.1"})
        self.assertEqual(response.status_code, 403)

    def test_invalid_secret_key(self):
        response = self.app.get("/", headers={"X-Secret-Key": "invalid-key"})
        self.assertEqual(response.status_code, 401)

    def test_request_endpoint(self):
        url = 'https://www.google.com'
        headers = {"X-Forwarded-For": "127.0.0.1", "X-Secret-Key": "my-secret-key"}
        response = self.app.post('/request', data=dict(url=url), headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
        url = 'invalid_url'
        headers={"X-Forwarded-For": "127.0.0.1", "X-Secret-Key": "my-secret-key"}
        response = self.app.post('/request', data=dict(url=url), headers=headers)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
