# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precip',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('precipitation', models.DecimalField(blank=True, db_column='Precipitation', decimal_places=2, max_digits=10, null=True)),
                ('snowdepth', models.DecimalField(blank=True, db_column='SnowDepth', decimal_places=2, max_digits=10, null=True)),
                ('snowfall', models.DecimalField(blank=True, db_column='SnowFall', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'precip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Severe',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('blowingsnow', models.IntegerField(blank=True, db_column='BlowingSnow', null=True)),
                ('drizzle', models.IntegerField(blank=True, db_column='Drizzle', null=True)),
                ('dust_ash', models.IntegerField(blank=True, db_column='Dust_Ash', null=True)),
                ('fog', models.IntegerField(blank=True, db_column='Fog', null=True)),
                ('freezingdrizzle', models.IntegerField(blank=True, db_column='FreezingDrizzle', null=True)),
                ('freezingrain', models.IntegerField(blank=True, db_column='FreezingRain', null=True)),
                ('glaze_rime', models.IntegerField(blank=True, db_column='Glaze_Rime', null=True)),
                ('groundfog', models.IntegerField(blank=True, db_column='GroundFog', null=True)),
                ('hail', models.IntegerField(blank=True, db_column='Hail', null=True)),
                ('heavyfog', models.IntegerField(blank=True, db_column='HeavyFog', null=True)),
                ('highwinds', models.IntegerField(blank=True, db_column='HighWinds', null=True)),
                ('icefog', models.IntegerField(blank=True, db_column='IceFog', null=True)),
                ('sleet', models.IntegerField(blank=True, db_column='Sleet', null=True)),
                ('mist', models.IntegerField(blank=True, db_column='Mist', null=True)),
                ('rain', models.IntegerField(blank=True, db_column='Rain', null=True)),
                ('smokehaze', models.IntegerField(blank=True, db_column='SmokeHaze', null=True)),
                ('snow', models.IntegerField(blank=True, db_column='Snow', null=True)),
                ('thunder', models.IntegerField(blank=True, db_column='Thunder', null=True)),
                ('tornado', models.IntegerField(blank=True, db_column='Tornado', null=True)),
            ],
            options={
                'db_table': 'severe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('tavg', models.DecimalField(blank=True, db_column='TAVG', decimal_places=2, max_digits=10, null=True)),
                ('tmax', models.DecimalField(blank=True, db_column='TMAX', decimal_places=2, max_digits=10, null=True)),
                ('tmin', models.DecimalField(blank=True, db_column='TMIN', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'temp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherDates',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('day', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'weather_dates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wind',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('averagewindspeed', models.DecimalField(blank=True, db_column='AverageWindSpeed', decimal_places=2, max_digits=10, null=True)),
                ('wsfg', models.DecimalField(blank=True, db_column='WSFG', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'wind',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
    ]