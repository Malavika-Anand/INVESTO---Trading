# Generated by Django 4.0.5 on 2022-06-15 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='balance1',
        ),
        migrations.RemoveField(
            model_name='details',
            name='live_bitcoin_price',
        ),
        migrations.RemoveField(
            model_name='details',
            name='live_bitcoin_price1',
        ),
        migrations.RemoveField(
            model_name='details',
            name='total_received1',
        ),
        migrations.RemoveField(
            model_name='details',
            name='total_sent1',
        ),
    ]
