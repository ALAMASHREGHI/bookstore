from django.contrib import admin
from .models import Book, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'active', ]
    inlines = [CommentInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'author', 'stars', 'active', ]

