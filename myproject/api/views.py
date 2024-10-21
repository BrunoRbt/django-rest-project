from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Author, Book
from rest_framework import viewsets
from .serializers import AuthorSerializer

def book_list(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)  # 10 livros por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj})

@login_required
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def home(request):
    return HttpResponse("Welcome to the home page!")

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
