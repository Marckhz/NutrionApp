# Generated by Django 3.0.3 on 2020-02-12 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutriologist', '0006_auto_20200212_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='place',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_hour',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='title',
        ),
    ]
