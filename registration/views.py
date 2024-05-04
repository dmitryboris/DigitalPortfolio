from django.shortcuts import render


def login(request):
    return render(request, 'registration/login.html')


def signup(request):
    return render(request, 'registration/signup.html')


def forget(request):
    return render(request, 'registration/forget.html')
