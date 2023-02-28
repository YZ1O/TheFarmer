from django.urls import path
from . import   views

app_name='main'


urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('cart/', views.view_cart, name='cart_page'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/', views.product_page, name='product_page'),

]
