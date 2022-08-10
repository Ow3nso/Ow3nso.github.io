# Generated by Django 4.0.5 on 2022-07-08 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_remove_patient_gender_delete_diagnosis_delete_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('age', models.IntegerField()),
                ('residence', models.CharField(max_length=200)),
                ('kin', models.CharField(max_length=200)),
                ('kincontacts', models.IntegerField()),
                ('datejoin', models.DateTimeField(auto_now_add=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.TextField()),
                ('management', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patient')),
            ],
        ),
    ]