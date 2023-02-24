from django.shortcuts import render
from django.http import HttpRequest

def add_product(request:HttpRequest):
    return render(request, 'farmer/add_product.html')


