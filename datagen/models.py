from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Country(models.Model):
    class Meta:
        db_table = 'Country'
    countryCode = models.CharField(max_length=3, primary_key=True)
    countryName = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    def getCountryCode(self):
        return self.countryCode
    def getCountryName(self):
        return self.countryName
    def getNationality(self):
        return self.nationality
    def __str__(self):
        return self.countryCode + " " + self.countryName + " " + self.nationality

@python_2_unicode_compatible
class Race(models.Model):
    class Meta:
        db_table = 'Race'
    raceId = models.IntegerField(primary_key=True)
    raceDesc = models.CharField(max_length=256)
    def getRaceId(self):
        return self.raceId
    def getRaceDesc(self):
        return self.raceDesc
    def __str__(self):
        return str(self.raceId) + " " + self.raceDesc

@python_2_unicode_compatible
class FirstName(models.Model):
    class Meta:
        db_table = 'FirstName'
    firstNameId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=256)
    gender = models.CharField(max_length=1)
    raceId = models.ForeignKey(Race, on_delete=models.CASCADE)
    def getFirstNameId(self):
        return self.firstNameId
    def getFirstName(self):
        return self.firstName
    def getGender(self):
        return self.gender
    def getRace(self):
        return Race.getRaceDesc(self.raceId)
    def __str__(self):
        return str(self.firstNameId) + " " + self.firstName + " " + self.gender + " " + self.getRace()

@python_2_unicode_compatible
class LastName(models.Model):
    class Meta:
        db_table = 'LastName'
    lastNameId = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=256)
    raceId = models.ForeignKey(Race, on_delete=models.CASCADE)
    def getLastNameId(self):
        return self.lastNameId
    def getLastName(self):
        return self.lastName
    def getRace(self):
        return Race.getRaceDesc(self.raceId)
    def __str__(self):
        return str(self.lastNameId) + " " + self.lastName + " " + self.getRace()

@python_2_unicode_compatible
class CountryRace(models.Model):
    class Meta:
        db_table = 'CountryRace'
    countryCode = models.ForeignKey(Country, on_delete=models.CASCADE)
    raceId = models.ForeignKey(Race, on_delete=models.CASCADE)
    def getCountryCode(self):
        return self.countryCode
    def getRace(self):
        return Race.getRaceDesc(self.raceId)
    def __str__(self):
        return self.countryCode + " " + self.getRace()