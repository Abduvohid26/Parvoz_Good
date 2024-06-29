from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    cover_pic = models.ImageField(default='default_cover_pic.png', upload_to='books_images')

    def __str__(self) -> str:
        return f'{self.author.first_name} {self.title}'
    

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    def __str__(self) -> str:
        return self.first_name
    

class BookComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    star_given = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(5)])
    creted_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.comment
