# Generated by Django 4.0.5 on 2022-07-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_patient_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
