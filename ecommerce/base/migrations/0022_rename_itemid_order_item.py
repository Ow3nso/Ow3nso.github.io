# Generated by Django 4.0.5 on 2022-08-03 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_order_itemid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='itemid',
            new_name='item',
        ),
    ]
