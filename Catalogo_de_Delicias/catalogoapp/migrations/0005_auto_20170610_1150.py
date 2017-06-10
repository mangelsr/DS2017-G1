from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0004_auto_20170607_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Restaurant', 'verbose_name_plural': 'Restaurants'},
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='adress',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_choice',
            field=models.CharField(choices=[('Aperitivo', 'Aperitivo'), ('Plato Fuerte', 'Plato Fuerte'), ('Postre', 'Postre')], default='A', max_length=20),
        ),
        migrations.AlterField(
            model_name='dish',
            name='temperature',
            field=models.CharField(choices=[('Frio', 'Frio'), ('Caliente', 'Caliente')], default='C', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Cliente', 'Cliente'), ('Ayudante', 'Ayudante'), ('Administrador', 'Administrador')], default='C', max_length=20),
        ),
    ]
