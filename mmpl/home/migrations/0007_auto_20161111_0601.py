# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20161111_0559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copyright',
            old_name='body',
            new_name='copyright',
        ),
    ]