# Generated by Django 4.0.6 on 2022-10-13 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_cartitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]
