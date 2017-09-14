# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0014_auto_20170913_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='mail_1',
            field=models.CharField(max_length=200, blank=True, verbose_name='email №1(обязательное поле)', null=True),
        ),
    ]
