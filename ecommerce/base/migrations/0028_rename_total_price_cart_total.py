# Generated by Django 4.0.5 on 2022-08-08 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_cart_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total_price',
            new_name='total',
        ),
    ]