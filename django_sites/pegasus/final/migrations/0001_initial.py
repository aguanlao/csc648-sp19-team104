# Generated by Django 2.1.7 on 2019-05-08 04:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicile',
            fields=[
                ('residence_id', models.AutoField(primary_key=True, serialize=False)),
                ('residence_type', models.CharField(choices=[('apartment', 'Apartment'), ('house', 'House'), ('room', 'Room'), ('garage', 'Garage'), ('in_law_unit', 'In-Law Unit'), ('other', 'Other')], max_length=50)),
                ('bed_count', models.IntegerField()),
                ('bath_count', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
                ('size', models.IntegerField()),
                ('creation_time', models.DateField(default=django.utils.timezone.now, editable=False)),
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
            ],
            options={
                'db_table': 'final_residences',
            },
        ),
    ]
