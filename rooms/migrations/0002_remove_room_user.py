# Generated by Django 4.2.1 on 2023-05-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
    ]
