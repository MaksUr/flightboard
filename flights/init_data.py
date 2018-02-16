import json
from datetime import timedelta, timezone
from json import JSONDecodeError
from random import randint, choice

import pytz
from django.utils import timezone
from os.path import join, isfile
from pytz import common_timezones

from flightboard.settings import BASE_DIR
from flights.constants import SCHEDULE_FLIGHT_STATUS_CHOICES
from flights.models import City, Airport, Airline, Flight, ScheduleFlight


IATA_DATA_FOLDER = join(BASE_DIR, 'flights', 'iata_data')
AIRLINES_DATA_FILE = join(IATA_DATA_FOLDER, 'airlines.json')
AIRPORTS_DATA_FILE = join(IATA_DATA_FOLDER, 'airports.json')


def open_json_file(fp):
    try:
        with open(fp, 'r') as f:
            try:
                res = json.load(f)
            except JSONDecodeError:
                return None
            else:
                return res
    except FileNotFoundError:
        return None


def create_airlines():
    airlines = open_json_file(AIRLINES_DATA_FILE)
    if airlines:
        for airline in airlines:
            Airline.objects.get_or_create(name=airline['name'], code=airline['iata'])


def create_airports():
    airports = open_json_file(AIRPORTS_DATA_FILE)
    if airports:
        for airport in airports:
            airport_data = airports[airport]
            if airport_data['iata'] and (airport_data['city'] or airport_data['state']):
                city, created = City.objects.get_or_create(
                    name=airport_data['city'] or airport_data['state'],
                    country_code=airport_data['country'],
                    timezone=airport_data['tz']
                )
                Airport.objects.get_or_create(
                    name=airport_data['name'],
                    code=airport_data['iata'],
                    city=city
                )


def get_duration(tz):

    if "America" in tz:
        return timedelta(hours=randint(12, 18), minutes=randint(0, 60))
    elif "Pacific" in tz:
        return timedelta(hours=randint(14, 19), minutes=randint(0, 60))
    elif "Atlantic" in tz:
        return timedelta(hours=randint(12, 16), minutes=randint(0, 60))
    elif "Europe" in tz:
        return timedelta(hours=randint(1, 5), minutes=randint(0, 60))
    elif "Africa" in tz:
        return timedelta(hours=randint(4, 8), minutes=randint(0, 60))
    elif "Australia" in tz:
        return timedelta(hours=randint(8, 14), minutes=randint(0, 60))
    elif "Arctic" in tz:
        return timedelta(hours=randint(3, 7), minutes=randint(0, 60))
    elif "Indian" in tz:
        return timedelta(hours=randint(12, 16), minutes=randint(0, 60))
    elif "Asia" in tz:
        return timedelta(hours=randint(0, 12), minutes=randint(0, 60))
    elif "Antarctica" in tz:
        return timedelta(hours=randint(12, 18), minutes=randint(0, 60))
    else:
        raise ValueError('Wrong timezone.')


def create_flights(count=30, location_airport='SVX'):
    location_airport = Airport.objects.get(code=location_airport)
    for f in range(count):
        number = randint(1, 10 ** 4 - 2)
        airline = Airline.objects.order_by('?').first()
        airport = Airport.objects.exclude(id=location_airport.id).order_by('?').first()
        duration = get_duration(airport.city.timezone.zone)
        Flight.objects.create(
            number=number,
            airline=airline,
            departure=location_airport,
            arrival=airport,
            duration=duration
        )

        Flight.objects.create(
            number=number+choice((-1, 1)),
            airline=airline,
            departure=airport,
            arrival=location_airport,
            duration=duration
        )


def create_schedule_flight():
    for f in Flight.objects.all():
        t_delta = timedelta(hours=randint(-70, 70), minutes=randint(0, 60))
        ScheduleFlight.objects.create(
            time_of_departure=timezone.now() + t_delta,
            status=choice(
                [val for val, label in SCHEDULE_FLIGHT_STATUS_CHOICES]
            ),
            flight=f
        )


def init():
    create_airlines()
    create_airports()
    create_flights()
    create_schedule_flight()
