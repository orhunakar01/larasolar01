# Generated by Django 3.0.8 on 2020-07-22 09:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0018_auto_20200721_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='AtanmaTarihi',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2020, 7, 22, 9, 49, 23, 55230, tzinfo=utc), verbose_name='Atanma Tarihi'),
        ),
    ]
