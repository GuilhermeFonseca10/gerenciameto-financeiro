from django.urls import reverse
from django.test import TestCase

class TestLucroUrl(TestCase):
    def test_lucros(self):
        response = self.client.get(reverse('lucro_list'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get(reverse('lucro_create'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.get(reverse('lucro_delete', kwargs={'pk' : 1}))
        self.assertEqual(response.status_code, 200)