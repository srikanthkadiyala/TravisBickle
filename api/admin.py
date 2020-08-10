from django.contrib import admin

from .models import Country, City, Sector, SubSector

# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Sector)
admin.site.register(SubSector)
