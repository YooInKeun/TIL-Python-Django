# Generated by Django 2.1.7 on 2019-04-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcount', '0010_auto_20190403_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='word_all_count',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='record',
            name='word_count',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
