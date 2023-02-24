from django.shortcuts import render
from django.http import  HttpRequest

def login_page(request:HttpRequest):
    return render(request, 'accounts/login.html')


def register_page(request:HttpRequest):
    return render(request, 'accounts/register.html')