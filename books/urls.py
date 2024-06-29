from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('author/', views.AuthorView.as_view(), name='author'),
    path('author/add/', views.AuthorAddView.as_view(), name='author_add'),
    path('', views.BookView.as_view(), name='book'),
    path('add/', views.BookAddView.as_view(), name='book_add'),
    path('<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<int:id>/comment/', views.BookCommentView.as_view(), name='book_comment')
]
