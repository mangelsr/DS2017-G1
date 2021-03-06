# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0011_dish_dish_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Lunch',
                'verbose_name_plural': 'Lunches',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('include_dessert', models.BooleanField()),
                ('include_juice', models.BooleanField()),
                ('cost', models.FloatField()),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name': 'Payment Method',
                'verbose_name_plural': 'Payment Methods',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.TextField(max_length=7)),
                ('font', models.TextField()),
                ('size', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Style',
                'verbose_name_plural': 'Styles',
            },
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='dishtemperature',
            options={'verbose_name': 'Temperature', 'verbose_name_plural': 'Temperatures'},
        ),
        migrations.AlterModelOptions(
            name='dishtype',
            options={'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AddField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='offer_lunch',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ExcecutiveLunch',
            fields=[
                ('lunch_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalogoapp.Lunch')),
                ('dessert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dessert', to='catalogoapp.Dish')),
                ('juice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juice', to='catalogoapp.Dish')),
            ],
            bases=('catalogoapp.lunch',),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogoapp.Profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='lunch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogoapp.Lunch'),
        ),
        migrations.AddField(
            model_name='lunch',
            name='main_curse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_curse', to='catalogoapp.Dish'),
        ),
        migrations.AddField(
            model_name='lunch',
            name='soup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soup', to='catalogoapp.Dish'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='style',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='catalogoapp.Style'),
            preserve_default=False,
        ),
    ]
