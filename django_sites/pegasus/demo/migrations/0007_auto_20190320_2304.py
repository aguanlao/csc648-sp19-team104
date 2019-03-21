# Generated by Django 2.1.7 on 2019-03-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20190320_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='domicile',
            name='city',
            field=models.CharField(default='nocity', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domicile',
            name='state',
            field=models.CharField(default='nostate', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domicile',
            name='zip',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
