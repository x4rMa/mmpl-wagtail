# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_footerabout'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FooterAbout',
            new_name='AboutFooter',
        ),
    ]