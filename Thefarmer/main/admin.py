from django.contrib import admin
from .models import Product , Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('farmer_owner', 'name', 'description', 'Weight' , 'price' , 'created_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_order' , 'created_at' , 'total_price' , 'number_of_products')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
