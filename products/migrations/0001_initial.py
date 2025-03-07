# Generated by Django 5.1.6 on 2025-03-03 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartegory_name', models.CharField(max_length=100, unique=True)),
                ('cartegory_image', models.ImageField(default='cartegories/kettle.png', upload_to='cartegories_group/')),
            ],
        ),
        migrations.CreateModel(
            name='CartegoryGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('cartegory_image', models.ImageField(default='cartegories/kettle.png', upload_to='cartegories_group/')),
                ('cartegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cartegory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('brand', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='products_image')),
                ('item_number', models.IntegerField()),
                ('number_bought', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('product_details', models.TextField()),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('offer', models.BooleanField(default=False)),
                ('trending', models.BooleanField(default=False)),
                ('calculated_discount', models.IntegerField(default=0)),
                ('exclusive', models.BooleanField(default=False)),
                ('cartegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cartegory', to_field='cartegory_name')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('review', models.TextField(default='best quality and looks legit')),
                ('star', models.IntegerField(default=0)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
