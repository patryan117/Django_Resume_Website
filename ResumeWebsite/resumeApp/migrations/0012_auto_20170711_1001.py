# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-11 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0011_generalinfo_privacy_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='privacy_policy',
            field=models.TextField(max_length=10000),
        ),
    ]
