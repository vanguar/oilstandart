# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0004_auto_20170912_1246'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nameoftheorganization',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='company_nameorganizacion',
            new_name='company',
        ),
    ]
