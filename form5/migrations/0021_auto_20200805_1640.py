# Generated by Django 3.0.8 on 2020-08-05 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form5', '0020_auto_20200805_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form5',
            name='faturaVade',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fatura Vadesi'),
        ),
    ]
