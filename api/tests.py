from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Author

class AuthorViewSetTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', age=45)
        self.url = reverse('author-list')

    def test_get_authors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        data = {'name': 'Jane Doe', 'age': 30}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
