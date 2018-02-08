from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField, ForeignKey

from flights.constants import FLIGHT_NUMBER_KEY, AIRLINE_NAME_KEY, AIRLINE_CODE_KEY, \
    AIRLINE_VERBOSE_NAME, AIRLINE_VERBOSE_NAME_PLURAL, FLIGHT_VERBOSE_NAME, FLIGHT_VERBOSE_NAME_PLURAL, \
    CITY_VERBOSE_NAME, CITY_VERBOSE_NAME_PLURAL, CITY_NAME_KEY, CITY_CODE_KEY, AIRPORT_VERBOSE_NAME, \
    AIRPORT_VERBOSE_NAME_PLURAL, AIRPORT_NAME_KEY, AIRPORT_CODE_KEY
from flights.validators import flight_number_validate


class City(models.Model):
    class Meta:
        verbose_name = CITY_VERBOSE_NAME
        verbose_name_plural = CITY_VERBOSE_NAME_PLURAL
    name = CharField(CITY_NAME_KEY, max_length=60)
    code = CharField(CITY_CODE_KEY, max_length=3)  # IATA 3-letter city code
    # timezone = TimeZoneField(CITY_TIMEZONE_KEY)  TODO: add timezone


class Airport(models.Model):
    class Meta:
        verbose_name = AIRPORT_VERBOSE_NAME
        verbose_name_plural = AIRPORT_VERBOSE_NAME_PLURAL
    name = CharField(AIRPORT_NAME_KEY, max_length=60)
    code = CharField(AIRPORT_CODE_KEY, max_length=3)  # IATA 3-letter airport code
    city = ForeignKey(City, verbose_name=City._meta.verbose_name)


class Airline(models.Model):
    class Meta:
        verbose_name = AIRLINE_VERBOSE_NAME
        verbose_name_plural = AIRLINE_VERBOSE_NAME_PLURAL
    name = CharField(AIRLINE_NAME_KEY, max_length=60)
    code = CharField(AIRLINE_CODE_KEY, max_length=2)  # IATA 2-letter code


class Flight(models.Model):
    class Meta:
        verbose_name = FLIGHT_VERBOSE_NAME
        verbose_name_plural = FLIGHT_VERBOSE_NAME_PLURAL
    number = IntegerField(FLIGHT_NUMBER_KEY, validators=[flight_number_validate])
    airline = ForeignKey(Airline, verbose_name=Airline._meta.verbose_name)
