# Generated by Django 5.2.4 on 2025-08-01 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='longitude',
        ),
    ]
