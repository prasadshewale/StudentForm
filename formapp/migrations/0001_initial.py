# Generated by Django 3.1.7 on 2021-10-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('semail', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pemail', models.CharField(max_length=100)),
                ('sfname', models.CharField(max_length=100)),
                ('slname', models.CharField(max_length=100)),
                ('pfname', models.CharField(max_length=100)),
                ('plname', models.CharField(max_length=100)),
                ('sphone', models.CharField(max_length=100)),
                ('pphone', models.CharField(max_length=100)),
                ('sadd', models.CharField(max_length=100)),
                ('padd', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('SSC', models.CharField(max_length=100)),
                ('HSC', models.CharField(max_length=100)),
            ],
        ),
    ]