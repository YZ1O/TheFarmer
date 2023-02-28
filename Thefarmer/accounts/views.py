from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from farmer.models import Farmer
from customer.models import Customer

from django.http import  HttpRequest

def login_page(request:HttpRequest):

    loggin_msg = None
    
    if request.method == "POST":
        #authenticate user credentials
        user = authenticate(request, username= request.POST["username"], password = request.POST["password"] )

        if user is not None:
            #login user
            login(request, user)
            return redirect("main:home_page")
        else:
            loggin_msg = "Please Use correct Credentials"

    return render(request, 'accounts/login.html' , {"msg" : loggin_msg})


def logout_page(request:HttpRequest):
    logout(request)
    return redirect('main:home_page')


def register_page(request:HttpRequest):
       
    if request.method == "POST":
        if request.POST.get("user_type") == "farmer":
            the_user = User.objects.create_user(
                username=request.POST["username"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=request.POST["password"]
                )
            the_user.save()
            new_farmer=Farmer.objects.create(user=the_user ,phone = request.POST["phone"])
            new_farmer.save()
        else:
            the_user = User.objects.create_user(
                username=request.POST["username"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=request.POST["password"]
                )
            the_user.save()
            new_customer=Customer.objects.create(user=the_user,phone = request.POST["phone"])

            new_customer.save()
            
            # return if POST
        return redirect("accounts:login_page")
        # return function
    return render(request, 'accounts/register.html')


def reset_password(request:HttpRequest):
    User.objects.get(email=request.POST["email"]).set_password('password').save()
    return render(request, 'accounts/reset_password.html')

