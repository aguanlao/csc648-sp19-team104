# Generated by Django 2.1.7 on 2019-04-18 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0013_auto_20190417_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unverifieduser',
            name='cleanliness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='unverifieduser',
            name='partiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='unverifieduser',
            name='socialness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='cleanliness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='partiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='verifieduser',
            name='socialness',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
