# Generated by Django 3.0.3 on 2020-02-13 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriologist', '0016_auto_20200213_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='age',
            field=models.IntegerField(),
        ),
    ]