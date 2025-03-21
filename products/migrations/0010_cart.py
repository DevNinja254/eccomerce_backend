# Generated by Django 5.1.6 on 2025-03-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_cartegory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('image', models.URLField()),
                ('itemId', models.IntegerField()),
                ('itemnumber', models.IntegerField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('title', models.CharField(max_length=150)),
            ],
        ),
    ]
