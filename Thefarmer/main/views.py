from django.shortcuts import render , redirect
from django.http import  HttpRequest
from .models import Product


def home_page(request:HttpRequest):
    return render(request, 'main/home_page.html')

def product_page(request:HttpRequest):

    products = Product.objects.all()
    context = {'products': products,}

    return render(request, 'main/product_page.html',context)

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart_page', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart_page'] = cart
    return redirect('main:cart_page')


def remove_from_cart(request, product_id):
    cart = request.session.get('main:cart_page', {})
    if cart.get(product_id):
        del cart[product_id]
        request.session['main:cart_page'] = cart
    return redirect('main:cart_page')


def view_cart(request):
    cart = request.session.get('cart_page', {})
    items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        item_total = product.price * quantity
        total += item_total
        items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })
    return render(request, 'main/cart_page.html', {'items': items, 'total': total})

