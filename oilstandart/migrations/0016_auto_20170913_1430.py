# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0015_auto_20170913_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='mail_1',
            field=models.CharField(verbose_name='email №1(обязательное поле)', max_length=200),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mail_2',
            field=models.CharField(verbose_name='email №2(необязательное поле)', max_length=200, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mail_3',
            field=models.CharField(verbose_name='email №3(необязательное поле)', max_length=200, blank=True, null=True),
        ),
    ]
