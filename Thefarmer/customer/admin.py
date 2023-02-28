from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']

    def username(self, obj):
        return obj.user.username
    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name
    def email(self, obj):
        return obj.user.email


admin.site.register(Customer, CustomerAdmin)

