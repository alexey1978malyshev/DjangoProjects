# Generated by Django 5.0.4 on 2024-05-27 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_results_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 27, 19, 20, 16, 569979)),
        ),
    ]
