# Generated by Django 4.0.5 on 2022-06-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_booking_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
