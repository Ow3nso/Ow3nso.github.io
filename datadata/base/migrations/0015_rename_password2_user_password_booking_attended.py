# Generated by Django 4.0.5 on 2022-07-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_booking_carbooked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password2',
            new_name='password',
        ),
        migrations.AddField(
            model_name='booking',
            name='Attended',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
