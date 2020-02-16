# Generated by Django 3.0.3 on 2020-02-12 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriologist', '0008_auto_20200212_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_hour',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
    ]