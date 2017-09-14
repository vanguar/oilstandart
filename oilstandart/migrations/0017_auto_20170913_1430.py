# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0016_auto_20170913_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='mail_1',
            field=models.CharField(verbose_name='email №1(обязательное поле)', max_length=200, null=True, blank=True),
        ),
    ]
