# Generated by Django 2.2.13 on 2021-11-05 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='prof',
        ),
    ]
