from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aboutus/', views.aboutus_page_view, name='aboutus'),
    path('contactus/', views.contactus_page_view, name='contactus'),
]
