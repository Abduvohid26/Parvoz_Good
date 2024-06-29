from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, BookForm, BookCommentForm
from django.views import View
from .models import Author, Book, BookComment
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorView(LoginRequiredMixin, View):
    def get(self, request):
        author = Author.objects.all()
        context = {'authors': author}
        return render(request, 'author.html', context=context)

class AuthorAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'author_add.html', context={'form': form})

    def post(self, request):
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("books:author")
        else:
            return render(request, 'author_add.html', context={'form': form})

class BookView(LoginRequiredMixin, View):
    def get(self, request):
        book = Book.objects.all()
        context = {'books': book}
        return render(request, 'book.html', context=context)

class BookAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book_add.html', context={'form': form})

    def post(self, request):
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("books:book")
        else:
            return render(request, 'book_add.html', context={'form': form})

class BookDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        form = BookCommentForm()
        context = {'book': book, 'form': form}
        return render(request, 'book_detail.html', context=context)
    

class BookCommentView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        form = BookCommentForm(data=request.POST, instance=book)
        if form.is_valid():
            BookComment.objects.create(
                user=request.user,
                book=book,
                comment=form.cleaned_data.get('comment'),
                star_given=form.cleaned_data['star_given']
            )
            return redirect(reverse('books:book_detail', kwargs={'id': book.id}))
        return render(request, 'book_detail.html', {'book': book, 'form': form})

