# Generated by Django 4.0.5 on 2022-07-01 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_booking_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='school',
        ),
        migrations.AlterField(
            model_name='members',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.booking'),
        ),
    ]
