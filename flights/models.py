from django.db import models
# Create your models here.
from django.db.models import CharField, IntegerField, ForeignKey, TimeField, DurationField, DateTimeField
from django.utils import timezone
from timezone_field import TimeZoneField

from flights.constants import FLIGHT_NUMBER_KEY, AIRLINE_NAME_KEY, AIRLINE_CODE_KEY, \
    AIRLINE_VERBOSE_NAME, AIRLINE_VERBOSE_NAME_PLURAL, FLIGHT_VERBOSE_NAME, FLIGHT_VERBOSE_NAME_PLURAL, \
    CITY_VERBOSE_NAME, CITY_VERBOSE_NAME_PLURAL, CITY_NAME_KEY, CITY_COUNTRY_CODE_KEY, AIRPORT_VERBOSE_NAME, \
    AIRPORT_VERBOSE_NAME_PLURAL, AIRPORT_NAME_KEY, AIRPORT_CODE_KEY, AIRPORT_CITY_KEY, CITY_TIMEZONE_KEY, \
    FLIGHT_AIRLINE_KEY, FLIGHT_DEPARTURE_KEY, FLIGHT_ARRIVAL_KEY, FLIGHT_DURATION_KEY, SCHEDULE_FLIGHT_VERBOSE_NAME, \
    SCHEDULE_FLIGHT_VERBOSE_NAME_PLURAL, SCHEDULE_FLIGHT_TIME_OF_DEPARTURE_KEY, \
    SCHEDULE_FLIGHT_STATUS_CHOICES, SCHEDULE_FLIGHT_FLIGHT_KEY, SCHEDULE_FLIGHT_STATUS_KEY
from flights.validators import flight_number_validate, country_code_validate, airport_code_validate, airline_code_validate


class City(models.Model):
    class Meta:
        verbose_name = CITY_VERBOSE_NAME
        verbose_name_plural = CITY_VERBOSE_NAME_PLURAL
    name = CharField(CITY_NAME_KEY, max_length=60)
    country_code = CharField(CITY_COUNTRY_CODE_KEY, max_length=3, validators=[country_code_validate])  # 2-letter city country_code
    timezone = TimeZoneField(verbose_name=CITY_TIMEZONE_KEY)

    def __str__(self):
        return self.name


class Airport(models.Model):
    class Meta:
        verbose_name = AIRPORT_VERBOSE_NAME
        verbose_name_plural = AIRPORT_VERBOSE_NAME_PLURAL
    name = CharField(AIRPORT_NAME_KEY, max_length=60)
    code = CharField(AIRPORT_CODE_KEY, max_length=3, validators=[airport_code_validate])  # IATA 3-letter airport code
    city = ForeignKey(City, verbose_name=AIRPORT_CITY_KEY)

    def __str__(self):
        return self.name

    def info(self):
        return '{city} ({airport})'.format(city=self.city.name, airport=self.code)


class Airline(models.Model):
    class Meta:
        verbose_name = AIRLINE_VERBOSE_NAME
        verbose_name_plural = AIRLINE_VERBOSE_NAME_PLURAL
    name = CharField(AIRLINE_NAME_KEY, max_length=60)
    code = CharField(AIRLINE_CODE_KEY, max_length=2, validators=[airline_code_validate])  # IATA 2-letter code

    def __str__(self):
        return self.name


class Flight(models.Model):
    class Meta:
        verbose_name = FLIGHT_VERBOSE_NAME
        verbose_name_plural = FLIGHT_VERBOSE_NAME_PLURAL
    number = IntegerField(FLIGHT_NUMBER_KEY, validators=[flight_number_validate])
    airline = ForeignKey(Airline, verbose_name=FLIGHT_AIRLINE_KEY)
    departure = ForeignKey(Airport, verbose_name=FLIGHT_DEPARTURE_KEY, related_name='airport_dep')
    arrival = ForeignKey(Airport, verbose_name=FLIGHT_ARRIVAL_KEY, related_name='airport_arr')
    duration = DurationField(FLIGHT_DURATION_KEY, )

    def __str__(self):
        return '{codename} ({dep}-{arr})'.format(
            codename=self.codename(),
            dep=self.departure.name,
            arr=self.arrival.name
        )

    def codename(self):
        return '{airline_code}-{flight_code:04}'.format(airline_code=self.airline.code, flight_code=self.number,)


class ScheduleFlight(models.Model):
    class Meta:
        verbose_name = SCHEDULE_FLIGHT_VERBOSE_NAME
        verbose_name_plural = SCHEDULE_FLIGHT_VERBOSE_NAME_PLURAL

    time_of_departure = DateTimeField(SCHEDULE_FLIGHT_TIME_OF_DEPARTURE_KEY)
    time_of_arrival = DateTimeField('Время прибытия')
    status = CharField(SCHEDULE_FLIGHT_STATUS_KEY, max_length=20, choices=SCHEDULE_FLIGHT_STATUS_CHOICES)
    flight = ForeignKey(Flight, verbose_name=SCHEDULE_FLIGHT_FLIGHT_KEY)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.time_of_arrival = self.time_of_departure + self.flight.duration
        return super().save(
            force_insert=False, force_update=False, using=None,
            update_fields=None)

    def __str__(self):
        return '{flight}: {time}'.format(flight=self.flight, time=self.time_of_departure)

    def arrival_status(self):
        d = timezone.now() - self.time_of_departure
        if d > self.flight.duration:
            return True
        else:
            return False



