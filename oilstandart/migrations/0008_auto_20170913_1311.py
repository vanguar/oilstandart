# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oilstandart', '0007_auto_20170912_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('address', models.CharField(verbose_name='Адрес(обязательное поле)', max_length=200)),
                ('phone_1', models.CharField(verbose_name='Телефон №1(обязательное поле)', max_length=200)),
                ('phone_2', models.CharField(verbose_name='Телефон №2(необязательное поле)', max_length=200)),
                ('phone_3', models.CharField(verbose_name='Телефон №3(необязательное поле)', max_length=200)),
                ('Working_hours', models.CharField(verbose_name='Время работы(обязательное поле)', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AlterModelOptions(
            name='priceandcompany',
            options={'verbose_name_plural': 'Цена продукта и название компании'},
        ),
        migrations.AlterField(
            model_name='priceandcompany',
            name='company',
            field=models.CharField(verbose_name='Название компании', max_length=200),
        ),
        migrations.AlterField(
            model_name='priceandcompany',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='priceandcompany',
            name='price',
            field=models.CharField(verbose_name='Цена за 1 литр', max_length=200),
        ),
        migrations.AlterField(
            model_name='priceandcompany',
            name='published_date',
            field=models.DateTimeField(verbose_name='Публикация даты', blank=True, null=True),
        ),
    ]
