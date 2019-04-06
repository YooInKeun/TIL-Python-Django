# Generated by Django 2.1.7 on 2019-04-03 01:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcount', '0018_auto_20190403_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='word',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='word_count',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=20),
        ),
    ]
