# Generated by Django 2.1.7 on 2019-05-08 05:13

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_birth', models.DateField(max_length=10)),
                ('physical_address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='final/profile_pictures')),
                ('creation_time', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('is_student', models.BooleanField()),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=500)),
                ('cleanliness', models.IntegerField(blank=True, null=True)),
                ('socialness', models.IntegerField(blank=True, null=True)),
                ('partiness', models.IntegerField(blank=True, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'final_unverified_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
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
