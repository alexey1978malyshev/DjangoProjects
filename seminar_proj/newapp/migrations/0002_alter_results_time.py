# Generated by Django 5.0.4 on 2024-05-11 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 12, 0, 56, 6, 218368)),
        ),
    ]