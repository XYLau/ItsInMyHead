from django.contrib import admin
from .models import Country, Race, FirstName, LastName, CountryRace, Address

# Register your models here.
admin.site.register(Country)
admin.site.register(Race)
admin.site.register(FirstName)
admin.site.register(LastName)
admin.site.register(CountryRace)
admin.site.register(Address)