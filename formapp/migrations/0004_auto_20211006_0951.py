# Generated by Django 3.1.7 on 2021-10-06 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0003_auto_20211006_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='HSC',
            new_name='HSC_marks',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='SSC',
            new_name='SSC_marks',
        ),
    ]
