# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0008_auto_20160712_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition',
            name='status',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
