# Generated by Django 4.0.6 on 2022-10-11 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_cart_subtotal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='todolist',
            new_name='cart',
        ),
    ]