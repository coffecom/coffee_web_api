# Generated by Django 3.1.5 on 2021-01-30 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0010_auto_20210129_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_available',
        ),
    ]
