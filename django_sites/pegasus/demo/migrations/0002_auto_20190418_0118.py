# Generated by Django 2.1.7 on 2019-04-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registereduser',
            name='extra',
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]