# Generated by Django 2.2.13 on 2021-11-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20211105_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='contenu',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
