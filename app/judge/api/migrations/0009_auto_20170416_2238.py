# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170414_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='source_path',
            field=models.FilePathField(path='/var/lib/judge/data/user_sources'),
        ),
    ]
