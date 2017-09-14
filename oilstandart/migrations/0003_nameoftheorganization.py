# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0002_auto_20170909_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nameoftheorganization',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
            ],
        ),
    ]
