# Generated by Django 4.0.5 on 2022-08-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_cart_total_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
    ]
