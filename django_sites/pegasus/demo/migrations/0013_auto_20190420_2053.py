# Generated by Django 2.1.7 on 2019-04-21 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0012_auto_20190420_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expiredlisting',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='expiredlistings',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='validlisting',
            name='residence',
        ),
        migrations.RemoveField(
            model_name='validlistings',
            name='residence',
        ),
        migrations.DeleteModel(
            name='ExpiredListing',
        ),
        migrations.DeleteModel(
            name='ExpiredListings',
        ),
        migrations.DeleteModel(
            name='ValidListing',
        ),
        migrations.DeleteModel(
            name='ValidListings',
        ),
    ]
