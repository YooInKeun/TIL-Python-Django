# Generated by Django 2.1.7 on 2019-04-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcount', '0006_remove_record_reated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='word_all_count',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='word_count',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
    ]
