# Generated by Django 4.1.7 on 2023-02-27 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_farmer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='phone',
        ),
    ]