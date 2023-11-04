from django import forms
from .models import Book, Comment


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'cover', 'active', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'stars', ]



