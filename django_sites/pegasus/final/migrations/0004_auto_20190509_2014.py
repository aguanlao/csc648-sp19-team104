# Generated by Django 2.1.7 on 2019-05-10 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0003_auto_20190507_2334'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='registereduser',
            table='final_all_registered_users',
        ),
        migrations.AlterModelTable(
            name='verifieduser',
            table='final_verified_users',
        ),
    ]