# Generated by Django 4.0.5 on 2022-08-03 16:22

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(default=django.contrib.auth.models.User, max_length=254),
        ),
    ]
