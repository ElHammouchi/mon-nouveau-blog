# Generated by Django 2.2.13 on 2021-11-05 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0008_auto_20211105_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_time',
            new_name='au',
        ),
    ]