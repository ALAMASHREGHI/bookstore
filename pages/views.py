from django.shortcuts import render


def home_page_view(request):
    return render(request, 'home.html')


def aboutus_page_view(request):
    return render(request, 'pages/aboutus.html')


def contactus_page_view(request):
    return render(request, 'pages/contactus.html')





