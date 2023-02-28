from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    phone = models.CharField(max_length=10 , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

