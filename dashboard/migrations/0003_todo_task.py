# Generated by Django 3.0.3 on 2020-03-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='task',
            field=models.CharField(default='', max_length=50),
        ),
    ]
