# Generated by Django 4.0.5 on 2022-07-09 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.DeleteModel(
            name='Diagnosis',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
