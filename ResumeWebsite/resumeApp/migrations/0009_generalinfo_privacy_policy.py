# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0008_auto_20170708_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='privacy_policy',
            field=models.TextField(default='Privacy policy copy goes here.', max_length=5000),
            preserve_default=False,
        ),
    ]
