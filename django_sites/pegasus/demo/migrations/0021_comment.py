# Generated by Django 2.1.7 on 2019-04-21 04:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0020_auto_20190420_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('creation_time', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('text', models.CharField(max_length=500)),
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('poster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comment_poster_id', to='demo.VerifiedUser', to_field='username')),
            ],
            options={
                'db_table': 'snn_comments',
            },
        ),
    ]