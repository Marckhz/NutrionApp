# Generated by Django 3.0.3 on 2020-02-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriologist', '0004_remove_patients_new_field'),
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
        migrations.AlterField(
            model_name='patients',
            name='age',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
