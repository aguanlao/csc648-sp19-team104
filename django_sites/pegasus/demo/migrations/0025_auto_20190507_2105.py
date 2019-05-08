# Generated by Django 2.1.7 on 2019-05-08 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0024_domicile_bed_bath'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='administrator',
            table='demo_admins',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='demo_snn_comments',
        ),
        migrations.AlterModelTable(
            name='disableduser',
            table='demo_disabled_users',
        ),
        migrations.AlterModelTable(
            name='domicile',
            table='demo_residences',
        ),
        migrations.AlterModelTable(
            name='expiredlisting',
            table='demo_expired_listings',
        ),
        migrations.AlterModelTable(
            name='landlord',
            table='demo_landlords',
        ),
        migrations.AlterModelTable(
            name='message',
            table='demo_snn_messages',
        ),
        migrations.AlterModelTable(
            name='page',
            table='demo_snn_pages',
        ),
        migrations.AlterModelTable(
            name='post',
            table='demo_snn_posts',
        ),
        migrations.AlterModelTable(
            name='registereduser',
            table='demo_unverified_users',
        ),
        migrations.AlterModelTable(
            name='startenant',
            table='demo_star_tenants',
        ),
        migrations.AlterModelTable(
            name='student',
            table='demo_students',
        ),
        migrations.AlterModelTable(
            name='validlisting',
            table='demo_valid_listings',
        ),
        migrations.AlterModelTable(
            name='verifieduser',
            table='demo_verified_users',
        ),
    ]
