# Generated by Django 3.0.8 on 2020-08-04 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form3', '0027_auto_20200803_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malzeme',
            name='Miktari',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='malzeme',
            name='birim_fiyati',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='malzeme',
            name='malzeme_adi',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='malzeme',
            name='olcu_birimi',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='malzeme',
            name='sira_no',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='malzeme',
            name='tarih',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='malzeme',
            name='tutar',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]