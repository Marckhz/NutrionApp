# Generated by Django 3.0.3 on 2020-02-12 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutriologist', '0013_auto_20200212_2228'),
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
            name='nutriologist',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='place',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='title',
        ),
    ]