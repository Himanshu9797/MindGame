# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-21 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MindGameApp', '0003_auto_20180121_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='fb_id',
        ),
    ]