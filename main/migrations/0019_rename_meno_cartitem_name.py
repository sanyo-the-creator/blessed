# Generated by Django 4.0.6 on 2022-10-11 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_cartitem_image_cartitem_meno_cartitem_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='meno',
            new_name='name',
        ),
    ]