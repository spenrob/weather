# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Precip(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    precipitation = models.DecimalField(db_column='Precipitation', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    snowdepth = models.DecimalField(db_column='SnowDepth', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    snowfall = models.DecimalField(db_column='SnowFall', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'precip'


class Severe(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    blowingsnow = models.IntegerField(db_column='BlowingSnow', blank=True, null=True)  # Field name made lowercase.
    drizzle = models.IntegerField(db_column='Drizzle', blank=True, null=True)  # Field name made lowercase.
    dust_ash = models.IntegerField(db_column='Dust_Ash', blank=True, null=True)  # Field name made lowercase.
    fog = models.IntegerField(db_column='Fog', blank=True, null=True)  # Field name made lowercase.
    freezingdrizzle = models.IntegerField(db_column='FreezingDrizzle', blank=True, null=True)  # Field name made lowercase.
    freezingrain = models.IntegerField(db_column='FreezingRain', blank=True, null=True)  # Field name made lowercase.
    glaze_rime = models.IntegerField(db_column='Glaze_Rime', blank=True, null=True)  # Field name made lowercase.
    groundfog = models.IntegerField(db_column='GroundFog', blank=True, null=True)  # Field name made lowercase.
    hail = models.IntegerField(db_column='Hail', blank=True, null=True)  # Field name made lowercase.
    heavyfog = models.IntegerField(db_column='HeavyFog', blank=True, null=True)  # Field name made lowercase.
    highwinds = models.IntegerField(db_column='HighWinds', blank=True, null=True)  # Field name made lowercase.
    icefog = models.IntegerField(db_column='IceFog', blank=True, null=True)  # Field name made lowercase.
    sleet = models.IntegerField(db_column='Sleet', blank=True, null=True)  # Field name made lowercase.
    mist = models.IntegerField(db_column='Mist', blank=True, null=True)  # Field name made lowercase.
    rain = models.IntegerField(db_column='Rain', blank=True, null=True)  # Field name made lowercase.
    smokehaze = models.IntegerField(db_column='SmokeHaze', blank=True, null=True)  # Field name made lowercase.
    snow = models.IntegerField(db_column='Snow', blank=True, null=True)  # Field name made lowercase.
    thunder = models.IntegerField(db_column='Thunder', blank=True, null=True)  # Field name made lowercase.
    tornado = models.IntegerField(db_column='Tornado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'severe'


class Temp(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tavg = models.DecimalField(db_column='TAVG', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmax = models.DecimalField(db_column='TMAX', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tmin = models.DecimalField(db_column='TMIN', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp'


class WeatherDates(models.Model):
    id = models.IntegerField(primary_key=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_dates'


class Wind(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    averagewindspeed = models.DecimalField(db_column='AverageWindSpeed', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    wsfg = models.DecimalField(db_column='WSFG', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wind'
