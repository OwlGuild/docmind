from django.test import TestCase
from django.urls import Resolver404, resolve


class HealthEndpointTests(TestCase):
    def test_health_returns_ok(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

    def test_health_names_the_service(self):
        response = self.client.get('/health/')
        self.assertEqual(response.json()['service'], 'docmind')

    def test_unknown_path_does_not_resolve(self):
        with self.assertRaises(Resolver404):
            resolve('/does-not-exist/')
