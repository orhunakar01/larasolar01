# Generated by Django 3.0.8 on 2020-07-24 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form5', '0003_auto_20200724_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='form5',
            name='bugun',
            field=models.DateField(default=datetime.date(2020, 7, 24)),
        ),
    ]
