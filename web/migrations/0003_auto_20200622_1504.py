# Generated by Django 3.0.4 on 2020-06-22 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200622_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='jhuData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2020, 6, 22, 15, 4, 56, 34671, tzinfo=utc))),
                ('csv_file', models.FileField(upload_to='data/uploads/JHU')),
            ],
        ),
        migrations.AlterField(
            model_name='table',
            name='csv_file',
            field=models.FileField(upload_to='data/upload'),
        ),
    ]
