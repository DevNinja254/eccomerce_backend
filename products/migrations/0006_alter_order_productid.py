# Generated by Django 5.1.6 on 2025-03-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_order_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='productId',
            field=models.IntegerField(default=1),
        ),
    ]
