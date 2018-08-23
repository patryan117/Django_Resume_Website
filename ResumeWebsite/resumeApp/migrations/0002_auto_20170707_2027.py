# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=64)),
                ('major', models.CharField(max_length=64)),
                ('minor', models.CharField(max_length=64)),
                ('semester', models.CharField(max_length=32)),
                ('year', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=5000)),
                ('executive_summary', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name_plural': 'General Info',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=5000)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.TextField(max_length=5000),
        ),
    ]
