# Generated by Django 3.1.5 on 2021-01-28 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0009_auto_20210129_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiptitem',
            old_name='item_id',
            new_name='item',
        ),
    ]