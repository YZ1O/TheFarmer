# Generated by Django 4.1.7 on 2023-02-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='phone',
            field=models.CharField(default='0555555555', max_length=10),
        ),
    ]
