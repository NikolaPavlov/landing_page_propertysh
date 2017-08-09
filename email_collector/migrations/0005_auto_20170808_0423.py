# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_collector', '0004_remove_subscribe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='be_client',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='be_host',
            field=models.BooleanField(default=False),
        ),
    ]