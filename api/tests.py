from django.test import TestCase
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', age=45)

    def test_author_creation(self):
        self.assertEqual(self.author.name, 'John Doe')
        self.assertEqual(self.author.age, 45)

class AuthorSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John Doe', age=45)

    def test_author_serializer(self):
        serializer = AuthorSerializer(self.author)
        data = serializer.data
        self.assertEqual(data['name'], 'John Doe')
        self.assertEqual(data['age'], 45)
