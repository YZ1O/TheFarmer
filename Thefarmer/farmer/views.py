from django.shortcuts import render
from django.http import HttpRequest
from main.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request:HttpRequest):
    if request.method == 'POST':
        # Get the currently logged in farmer
        farmer = request.user.farmer

        # Create a new Product instance with the farmer_owner set
        new_product = Product(
            farmer_owner=farmer,
            name=request.POST['name'],
            description=request.POST['description'],
            type=request.POST['type'],
            image=request.FILES['image'],
            Weight=request.POST['Weight'],
            price=request.POST['price'],
        )
        new_product.save()

    return render(request, 'farmer/add_product.html')
