# Generated by Django 3.0.8 on 2020-07-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0005_auto_20200715_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='Sorumlusu',
            field=models.CharField(choices=[('orhunakar', 'orhunakar'), ('semihbudak', 'semihbudak')], max_length=25, verbose_name='Sorumlu Kişiyi Ata'),
        ),
    ]
