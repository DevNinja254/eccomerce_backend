# Generated by Django 5.1.6 on 2025-03-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_product_description_alter_product_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_details',
            field=models.TextField(),
        ),
    ]
