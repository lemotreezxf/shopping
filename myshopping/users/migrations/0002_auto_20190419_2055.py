# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-19 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default='15837035590', max_length=50, verbose_name='联系方式'),
        ),
    ]
