# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-04 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20171204_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
    ]
