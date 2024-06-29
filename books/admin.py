from django.contrib import admin
from .models import Book, Author, BookComment

admin.site.register([Book, Author, BookComment])
