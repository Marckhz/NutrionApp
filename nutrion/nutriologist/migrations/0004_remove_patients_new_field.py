# Generated by Django 3.0.3 on 2020-02-12 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutriologist', '0003_auto_20200212_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='new_field',
        ),
    ]
