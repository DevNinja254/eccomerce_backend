# Generated by Django 5.1.6 on 2025-03-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
