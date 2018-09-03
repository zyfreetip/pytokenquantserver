# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-03 08:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blockuser', '0007_auto_20180830_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantPolicyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.CharField(max_length=20)),
                ('policy_start_time', models.DateTimeField()),
                ('policy_end_time', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'quant_policy_order',
                'db_table': 'quant_policy_order',
                'abstract': False,
                'managed': True,
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
