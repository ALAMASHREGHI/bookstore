from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    cover = models.ImageField(upload_to='covers/', blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])

class Comment(models.Model):
    BOOK_STARS = [
        ('1', 'bad'),
        ('2', 'normal'),
        ('3', 'good'),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    stars = models.CharField(max_length=10, choices=BOOK_STARS)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.book.id])
