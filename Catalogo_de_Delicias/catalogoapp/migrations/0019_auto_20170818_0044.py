# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0018_auto_20170817_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes_set', related_query_name='dish', to='catalogoapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='restaurant',
            field=models.ForeignKey(blank=True, help_text='Solo necesario si el rol es Ayudante', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_set', related_query_name='profiles', to='catalogoapp.Restaurant'),
        ),
    ]