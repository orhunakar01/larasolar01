# Generated by Django 3.0.8 on 2020-07-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0029_auto_20200724_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='Sorumlusu',
            field=models.CharField(choices=[('orhunakar', 'orhunakar'), ('yetkisiz', 'yetkisiz'), ('yetkisiz01', 'yetkisiz01')], max_length=25, verbose_name='Sorumlu Kişiyi Ata'),
        ),
    ]
