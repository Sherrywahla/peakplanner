# Generated by Django 4.2.19 on 2025-03-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
