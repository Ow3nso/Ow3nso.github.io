# Generated by Django 4.0.5 on 2022-08-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_order_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item',
            new_name='itemid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='landmark',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='order',
            name='town',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
