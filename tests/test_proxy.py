"""Tests."""

from flask_testing import TestCase
from proxy_server.proxy.app import app
import requests_mock

TEST_URL = 'https://example.com'

with open('tests/fixtures/example.html', 'r') as file:
    html_page = file.read()

with open('tests/fixtures/example-expected.html', 'r') as file:
    html_expected_text = file.read()


class BaseTestCase(TestCase):
    """Main test."""

    def create_app(self):
        app.config['TESTING'] = True
        app.config['PROXY_URL'] = TEST_URL
        return app

    def test_modify_content_if_text(self):
        with requests_mock.Mocker() as m:
            m.get(TEST_URL,
                  text=html_page,
                  headers={'Content-Type': 'text/html; charset=utf-8'})
            response = self.client.get('/')
            self.assertEqual(response.text, html_expected_text)

    def test_dont_modify_is_not_text(self):
        chars = 'letter'
        with requests_mock.Mocker() as m:
            m.get(TEST_URL,
                  text=chars,
                  headers={'Content-Type': 'text/css'})
            response = self.client.get('/')
            self.assertEqual(response.text, chars)

    def test_http_status(self):
        with requests_mock.Mocker() as m:
            m.get(TEST_URL,
                  status_code=404,
                  text='page not found',
                  headers={'Content-Type': 'text/html; charset=utf-8'})
            response = self.client.get('/')
            self.assert404(response)

    def test_content_type(self):
        content_type = 'text/plain; charset=utf-8'
        with requests_mock.Mocker() as m:
            m.get(TEST_URL,
                  text='nothing',
                  headers={'Content-Type': content_type})
            response = self.client.get('/')
            print(response.headers)
            self.assertEqual(response.headers['Content-Type'], content_type)
