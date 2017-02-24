from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
    class Meta:
        db_table = 'Country'
    countryCode = models.CharField(max_length=3, primary_key=True)
    countryName = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)

class Race(models.Model):
    class Meta:
        db_table = 'Race'
    raceId = models.IntegerField(primary_key=True)
    raceDesc = models.CharField(max_length=256)

class FirstName(models.Model):
    class Meta:
        db_table = 'FirstName'
    firstNameId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=256)
    gender = models.CharField(max_length=1)
    raceId = models.ForeignKey(Race, on_delete=models.CASCADE)

class LastName(models.Model):
    class Meta:
        db_table = 'LastName'
    lastNameId = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=256)
    raceId = models.ForeignKey(Race, on_delete=models.CASCADE)

class CountryRace(models.Model):
    class Meta:
        db_table = 'CountryRace'
        unique_together = (('countryCode', 'raceId'),)

    countryCode = models.ForeignKey(Country, on_delete=models.CASCADE)
    raceId = models.ForeignKey(Race, on_delete=models.CASCADE)