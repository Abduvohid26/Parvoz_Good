from django import forms
from .models import Book, Author, BookComment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'bio']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'description', 'isbn', 'cover_pic']
        

class BookCommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = ['comment', 'star_given']