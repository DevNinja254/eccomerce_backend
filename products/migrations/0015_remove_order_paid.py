# Generated by Django 5.1.6 on 2025-03-15 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_order_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
    ]
