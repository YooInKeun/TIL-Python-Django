# Generated by Django 2.1.7 on 2019-04-02 18:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcount', '0015_auto_20190403_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='word',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='record',
            name='word_count',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
    ]
