# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 21:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_auto_20170416_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='task_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]