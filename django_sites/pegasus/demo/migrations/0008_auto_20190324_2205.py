# Generated by Django 2.1.7 on 2019-03-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20190320_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domicile',
            name='size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='domicile',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]
