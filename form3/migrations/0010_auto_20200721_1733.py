# Generated by Django 3.0.8 on 2020-07-21 14:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0018_auto_20200721_1733'),
        ('form3', '0009_auto_20200721_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form3',
            name='Form33',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='form2.Form2'),
        ),
        migrations.AlterField(
            model_name='form3',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 21, 14, 33, 39, 310737, tzinfo=utc), verbose_name='Bugünkü Tarih'),
        ),
    ]
