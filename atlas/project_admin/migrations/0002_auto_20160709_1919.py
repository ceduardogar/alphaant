# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='contact',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project_admin.Contact'),
            preserve_default=False,
        ),
    ]
