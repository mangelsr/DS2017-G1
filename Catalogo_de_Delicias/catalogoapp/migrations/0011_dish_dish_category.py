# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0010_auto_20170628_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogoapp.DishCategory'),
        ),
    ]