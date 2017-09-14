# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0005_auto_20170912_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
