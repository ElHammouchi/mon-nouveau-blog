# Generated by Django 2.2.13 on 2021-11-05 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0006_auto_20211105_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
    ]
