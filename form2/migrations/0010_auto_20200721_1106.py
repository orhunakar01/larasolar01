# Generated by Django 3.0.8 on 2020-07-21 08:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0009_auto_20200721_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='AtanmaTarihi',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2020, 7, 21, 8, 6, 6, 914941, tzinfo=utc), verbose_name='Atanma Tarihi'),
        ),
    ]