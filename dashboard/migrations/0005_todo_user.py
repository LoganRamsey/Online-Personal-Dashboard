# Generated by Django 3.0.3 on 2020-03-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200328_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.CharField(default='', max_length=6),
        ),
    ]