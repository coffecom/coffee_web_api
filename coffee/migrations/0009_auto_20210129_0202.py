# Generated by Django 3.1.5 on 2021-01-28 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0008_auto_20210129_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptitem',
            name='receipt_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='coffee.receipt'),
        ),
    ]
