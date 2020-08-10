from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    currency = models.CharField(max_length=32, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name_plural = 'Countries'
        db_table = "countries"

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name_plural = 'Cities'
        db_table = "cities"

    def __str__(self):
        return self.name


class Sector(models.Model):
    mongo_sector_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name_plural = 'Sectors'
        db_table = "sector"

    def __str__(self):
        return self.name


class SubSector(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name_plural = 'SubSectors'
        db_table = "sub_sector"

    def __str__(self):
        return self.name