# Generated by Django 3.0.8 on 2020-08-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
