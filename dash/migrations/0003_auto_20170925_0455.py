# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20170925_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.TextField(null=True),
        ),
    ]
