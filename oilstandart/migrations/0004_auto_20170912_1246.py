# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0003_nameoftheorganization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nameoftheorganization',
            old_name='company_name',
            new_name='company_nameorganizacion',
        ),
    ]
