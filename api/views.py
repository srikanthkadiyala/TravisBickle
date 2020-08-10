from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Country, City, Sector, SubSector
from .serializers import CitySerializer, SubSectorSerializer


class GetCitiesFromCountry(APIView):

    def get(self, request, country, city):
        try:
            country = Country.objects.get(name__iexact=country)
        except Exception as e:
            return Response({
                'message': 'No Country Found with Given Name, Please Enter Valid Country Name',
                'error': e
            })
        cities = country.city_set.filter(name__icontains=city)
        city_serializer = CitySerializer(cities, many=True)
        return Response({
            'data': city_serializer.data
        })


class GetSectorsFromMongoSectorId(APIView):

    def get(self, request, mongo_sector_id):
        try:
            sector = Sector.objects.get(mongo_sector_id=mongo_sector_id)
        except Exception as e:
            return Response({'message': 'Please Enter Valid Id', 'error': e})
        sub_sector = sector.subsector_set.all()
        sub_sector_serializer = SubSectorSerializer(sub_sector, many=True)
        return Response({
            'data': sub_sector_serializer.data
        })
