# Generated by Django 4.0.6 on 2022-11-18 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_products_country_alter_wanted_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Wanted'},
        ),
        migrations.AlterModelOptions(
            name='wanted',
            options={'verbose_name_plural': 'Products'},
        ),
    ]
