import unittest
import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)


class APITestCase(unittest.TestCase):
    def setUp(self):
        # Initial settings
        token = os.environ.get('TOKEN_TEST')
        url = 'http://127.0.0.1:8080'

        self.base_url = url + '/api/v1/settings'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        }
        self.payload = {
            'email_notification': True,
            'max_revenue_amount': 81000,
            'sms_notification': False,
        }

        # Setting to test Unauthorized
        self.base_url_error = url + '/api/v2/settings'
        self.headers_error = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
        }

    def test_update_settings(self):
        # Sends a PUT request and expects to return a 204 code
        response = requests.put(
            self.base_url, headers=self.headers, data=json.dumps(self.payload)
        )
        self.assertEqual(response.status_code, 204)

    def test_get_settings(self):
        # Sends a GET request and expects to return a 200 code and json payload
        response = requests.get(self.base_url, headers=self.headers)
        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        self.assertEqual(response_json, self.payload)

    def test_get_settings_unauthorized_version(self):
        # Sends a GET request and expects to return a 401 code
        response = requests.get(self.base_url_error, headers=self.headers)
        self.assertEqual(response.status_code, 401)

    def test_get_settings_unauthorized_token(self):
        # Sends a GET request and expects to return a 401 code
        response = requests.get(self.base_url, headers=self.headers_error)
        self.assertEqual(response.status_code, 401)

    def test_put_settings_unauthorized_version(self):
        # Sends a PUT request and expects to return a 401 code
        response = requests.put(
            self.base_url_error,
            headers=self.headers,
            data=json.dumps(self.payload),
        )
        self.assertEqual(response.status_code, 401)

    def test_put_settings_unauthorized_token(self):
        # Sends a PUT request and expects to return a 401 code
        response = requests.put(
            self.base_url,
            headers=self.headers_error,
            data=json.dumps(self.payload),
        )
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
