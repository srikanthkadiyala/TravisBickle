from pymongo import MongoClient

from TravisBickle.settings import MONGO_DB, MONGO_AUTH, MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASS
from api.models import Country, City, Sector, SubSector


def establish_connection_to_mongo_db():
    url = "mongodb://{}:{}@{}:{}/{}?authSource={}".format(
        MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB, MONGO_AUTH
    )
    conn = MongoClient(url)
    db = conn.get_database()
    return db


def get_countries_and_cities_from_mongo_to_sqlite():
    db = establish_connection_to_mongo_db()
    table = db.geo
    table_name = table.find()
    for record in table_name:
        info = {}
        countries = Country.objects.all()
        for _record in countries:
            info[_record.name] = True
        if record['countryName'] in info:
            continue
        country = Country.objects.create(
            name=record['countryName'], code=record['countryCode'], currency=record['countryCurrency']
        )
        cities = record['cities']
        for city in cities:
            country.city_set.create(name=city)


def get_sectors_from_mongo_to_sqlite():
    db = establish_connection_to_mongo_db()
    table = db.sectors
    table_name = table.find()
    for record in table_name:
        sector = Sector.objects.create(
            mongo_sector_id=str(record['_id']), name=record['sectorName']
        )
        for _sector in record.get('subSectors'):
            sector.subsector_set.create(name=_sector)