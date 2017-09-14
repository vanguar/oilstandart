# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0011_auto_20170913_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone_2',
            field=models.CharField(verbose_name='Телефон №2(необязательное поле)', max_length=200),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone_3',
            field=models.CharField(verbose_name='Телефон №3(необязательное поле)', max_length=200),
        ),
    ]
