# Generated by Django 4.1.7 on 2023-02-26 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmer', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('farmer_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_products', models.IntegerField()),
                ('customer_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('products', models.ManyToManyField(to='main.product')),
            ],
        ),
    ]