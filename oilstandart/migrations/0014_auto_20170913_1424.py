# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0013_auto_20170913_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='mail_1',
            field=models.CharField(max_length=200, verbose_name='email №1(обязательное поле)', null=True, default=None, blank=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='mail_2',
            field=models.CharField(max_length=200, verbose_name='email №2(необязательное поле)', null=True, default=None, blank=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='mail_3',
            field=models.CharField(max_length=200, verbose_name='email №3(необязательное поле)', null=True, default=None, blank=True),
        ),
    ]
