from django.urls import path
from .import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('new/', views.book_create_view, name='book_create'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('comments/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
]
