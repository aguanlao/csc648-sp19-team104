# Generated by Django 2.1.7 on 2019-04-21 03:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20190420_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiredListings',
            fields=[
                ('creation_time', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('residence', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='demo.Domicile')),
                ('owner', models.CharField(max_length=15)),
                ('price', models.FloatField(max_length=10)),
                ('expire_time', models.DateField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'expired_listings',
            },
        ),
        migrations.CreateModel(
            name='ValidListings',
            fields=[
                ('creation_time', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('residence', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='demo.Domicile')),
                ('owner', models.CharField(max_length=15)),
                ('price', models.FloatField(max_length=10)),
                ('tenants', models.CharField(max_length=100)),
                ('pet_friendly', models.BooleanField()),
                ('pets_allowed', models.CharField(blank=True, max_length=100, null=True)),
                ('limit_tenant_count', models.IntegerField(blank=True, null=True)),
                ('current_tenant_count', models.IntegerField(blank=True, null=True)),
                ('amenities', models.CharField(blank=True, max_length=100, null=True)),
                ('utilities_included_rent', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('coordinates', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='demo/residence_pictures')),
            ],
            options={
                'db_table': 'valid_listings',
            },
        ),
        #migrations.RemoveField(
        #    model_name='expiredlisting',
        #    name='residence',
        #),
        #migrations.RemoveField(
        #    model_name='validlisting',
        #    name='residence',
        #),
        #migrations.DeleteModel(
        #    name='ExpiredListing',
        #),
        #migrations.DeleteModel(
        #    name='ValidListing',
        #),
    ]
