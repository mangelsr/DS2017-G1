# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0016_auto_20170816_1715'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExcecutiveLunch',
            new_name='ExecutiveLunch',
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
