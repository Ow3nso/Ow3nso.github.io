# Generated by Django 4.0.5 on 2022-07-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_booking_username_alter_members_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Username',
            field=models.CharField(max_length=200),
        ),
    ]
