# Generated by Django 3.0.3 on 2020-04-13 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200413_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='testint',
        ),
        migrations.AddField(
            model_name='todo',
            name='dueYear',
            field=models.IntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 3, 39, 228904, tzinfo=utc)),
        ),
    ]