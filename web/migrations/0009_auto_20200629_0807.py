# Generated by Django 3.0.7 on 2020-06-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20200629_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vndata',
            name='csv_file',
            field=models.FilePathField(path='data/VN'),
        ),
    ]