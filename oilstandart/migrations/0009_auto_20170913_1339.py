# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0008_auto_20170913_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Публикация даты'),
        ),
    ]
