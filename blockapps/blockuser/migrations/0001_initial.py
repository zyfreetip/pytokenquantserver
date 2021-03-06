# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 07:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DuiQiaoPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('huobi', '火币'), ('okex', 'OKEX'), ('fcoin', 'Fcoin')], help_text='请选择一个交易所', max_length=20, verbose_name='交易所')),
                ('accesskey', models.CharField(help_text='请填写您在交易所的api access key', max_length=100, verbose_name='Accesskey')),
                ('secretkey', models.CharField(help_text='请填写您在交易所的api secret key', max_length=100, verbose_name='SecretKey')),
                ('symbol', models.CharField(choices=[('btcusdt', 'BTC/USDT'), ('ethusdt', 'ETH/USDT')], help_text='请填写该交易所的交易对例如BTC/USDT', max_length=20, verbose_name='交易对')),
                ('max_buy_price', models.DecimalField(decimal_places=8, help_text='请填写该交易对的最高买入价格', max_digits=20, verbose_name='最高买入价格')),
                ('min_sell_price', models.DecimalField(decimal_places=8, help_text='请填写该交易对的最低卖出价格', max_digits=20, verbose_name='最低卖出价格')),
                ('start_time', models.DateTimeField(help_text='请填写您的交易策略运行开始时间', verbose_name='开始运行时间')),
                ('end_time', models.DateTimeField(help_text='请填写您的交易策略结束运行时间', verbose_name='结束运行时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='记录更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
                ('status', models.CharField(blank=True, choices=[('unstart', '未开始'), ('run', '运行中'), ('stop', '已停止')], default='unstart', help_text='策略运行状态', max_length=10, verbose_name='运行状态')),
                ('operation', models.IntegerField(blank=True, choices=[(0, '开启运行'), (1, '停止运行')], default=0, help_text='操作', verbose_name='操作')),
                ('base_volume', models.DecimalField(decimal_places=8, default=0, help_text='请填写交易对的币数量,比如BTC/USDT，就是BTC的数量', max_digits=100, verbose_name='base货币数量')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '对敲策略',
                'db_table': 'duiqiao',
                'abstract': False,
                'managed': True,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='QuantPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=5, default=0, max_digits=40, verbose_name='购买价格')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('exchanges', models.TextField(default='', verbose_name='支持交易所列表')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='记录更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录创建时间')),
            ],
            options={
                'verbose_name': 'quant_policy',
                'db_table': 'quant_policy',
                'abstract': False,
                'managed': True,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
