# Generated by Django 2.1.7 on 2019-04-02 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordcount', '0009_auto_20190403_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='word_all_countt',
        ),
        migrations.RemoveField(
            model_name='record',
            name='word_countt',
        ),
    ]
