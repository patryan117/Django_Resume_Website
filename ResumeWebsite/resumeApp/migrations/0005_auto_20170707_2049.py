# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0004_education_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='start_date',
            new_name='start_year',
        ),
        migrations.AddField(
            model_name='education',
            name='start_semester',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]