from django.shortcuts import render
from django.http import  HttpRequest

def login_page(request:HttpRequest):
    return render(request, 'accounts/login.html')

def register_page(request:HttpRequest):
    return render(request, 'accounts/register.html')

def reset_password(request:HttpRequest):
    return render(request, 'accounts/reset_password.html')

#work on it
#def logout_page(request:HttpRequest):
#    return render(request, 'accounts/logout.html')

#def profile_page(request:HttpRequest):
#    return render(request, 'accounts/profile.html')
