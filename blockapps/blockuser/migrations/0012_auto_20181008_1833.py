# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-08 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockuser', '0011_auto_20180928_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duiqiaopolicy',
            name='symbol',
            field=models.CharField(default='', help_text='请填写该交易所的交易对例如BTC/USDT', max_length=20, verbose_name='交易对'),
        ),
    ]
