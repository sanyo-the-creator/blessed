# Generated by Django 4.0.6 on 2022-10-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cart_products_user_orders_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]