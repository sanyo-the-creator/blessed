# Generated by Django 4.0.6 on 2022-10-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='color1',
            field=models.CharField(default='#FFFFFF', max_length=8),
        ),
        migrations.AddField(
            model_name='products',
            name='color2',
            field=models.CharField(default='#000000', max_length=8),
        ),
    ]
