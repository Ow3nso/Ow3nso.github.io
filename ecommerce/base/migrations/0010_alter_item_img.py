# Generated by Django 4.0.5 on 2022-07-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_item_category_alter_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(upload_to='photos'),
        ),
    ]