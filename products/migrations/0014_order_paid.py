# Generated by Django 5.1.6 on 2025-03-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_cart_item_number_cart_number_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
