# Generated by Django 4.0.6 on 2022-10-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_products_checked_products_problems'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
