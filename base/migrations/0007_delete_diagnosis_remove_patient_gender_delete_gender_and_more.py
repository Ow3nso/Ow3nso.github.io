# Generated by Django 4.0.5 on 2022-07-09 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_diagnosis_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Diagnosis',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]