from django.db import models
from farmer.models import Farmer
from customer.models import Customer




class Product(models.Model):
    farmer_owner = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    Weight = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)



class Order(models.Model):
    customer_order = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_products = models.IntegerField()

    

