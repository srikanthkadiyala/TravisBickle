from rest_framework import serializers

from .models import Country, City, Sector, SubSector


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ('created_on', 'updated_on')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        exclude = ('created_on', 'updated_on')


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        exclude = ('created_on', 'updated_on')


class SubSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSector
        exclude = ('created_on', 'updated_on')