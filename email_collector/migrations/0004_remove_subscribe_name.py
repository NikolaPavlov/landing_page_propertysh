# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 18:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_collector', '0003_auto_20170807_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='name',
        ),
    ]
