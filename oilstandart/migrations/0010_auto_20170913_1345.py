# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0009_auto_20170913_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='published_date',
        ),
    ]
