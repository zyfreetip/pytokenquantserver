# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereum', '0006_auto_20180428_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethereumblockmodel',
            name='total_difficulty',
            field=models.CharField(default=0, max_length=255, verbose_name='区块累计总难度'),
        ),
    ]
