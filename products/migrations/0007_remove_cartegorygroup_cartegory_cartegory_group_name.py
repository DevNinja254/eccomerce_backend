# Generated by Django 5.1.6 on 2025-03-10 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_order_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartegorygroup',
            name='cartegory',
        ),
        migrations.AddField(
            model_name='cartegory',
            name='group_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cartegory_group', to='products.cartegorygroup'),
        ),
    ]
