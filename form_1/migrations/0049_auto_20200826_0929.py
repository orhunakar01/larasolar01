# Generated by Django 3.0.8 on 2020-08-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0048_auto_20200820_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='FirmaAdi',
            field=models.CharField(choices=[], max_length=60, verbose_name='Firma Adı'),
        ),
    ]