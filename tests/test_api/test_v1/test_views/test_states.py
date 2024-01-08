import unittest
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch

from api.v1.views import app_views


class TestCitiesAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(app_views)
        self.client = self.app.test_client()

    def test_get_cities(self):
        with patch('models.storage.get') as mock_get:
            mock_get.return_value = None
            response = self.client.get('/states/1/cities')
            self.assertEqual(response.status_code, 404)

    def test_get_city(self):
        with patch('models.storage.get') as mock_get:
            mock_get.return_value = None
            response = self.client.get('/cities/1')
            self.assertEqual(response.status_code, 404)

    def test_delete_city(self):
        with patch('models.storage.get') as mock_get:
            mock_get.return_value = None
            response = self.client.delete('/cities/1')
            self.assertEqual(response.status_code, 404)

    def test_post_city(self):
        with patch('models.storage.get') as mock_get:
            mock_get.return_value = None
            response = self.client.post('/states/1/cities', json={'name': 'New City'})
            self.assertEqual(response.status_code, 404)

    def test_put_city(self):
        with patch('models.storage.get') as mock_get:
            mock_get.return_value = None
            response = self.client.put('/cities/1', json={'name': 'Updated City'})
            self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

