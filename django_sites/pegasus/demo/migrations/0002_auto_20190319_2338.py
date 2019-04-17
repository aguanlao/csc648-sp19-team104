# Generated by Django 2.1.7 on 2019-03-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisabledUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='domicile',
            name='price',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='owners',
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.FloatField(default=-1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='administrator',
            table='admins',
        ),
        migrations.AlterModelTable(
            name='domicile',
            table='residences',
        ),
        migrations.AlterModelTable(
            name='landlord',
            table='landlords',
        ),
        migrations.AlterModelTable(
            name='listing',
            table='listings',
        ),
        migrations.AlterModelTable(
            name='startenant',
            table='star_tenants',
        ),
        migrations.AlterModelTable(
            name='student',
            table='students',
        ),
        migrations.AlterModelTable(
            name='unverifieduser',
            table='unverified_users',
        ),
        migrations.AlterModelTable(
            name='verifieduser',
            table='verified_users',
        ),
    ]