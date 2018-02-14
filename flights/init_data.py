from datetime import timedelta, timezone
from random import randint, choice

import pytz
from django.utils import timezone
from pytz import common_timezones

from flights.constants import SCHEDULE_FLIGHT_STATUS_CHOICES
from flights.models import City, Airport, Airline, Flight, ScheduleFlight


def create_cities():
    FLIGHT_NUMBER = 15
    for time_zone in common_timezones:
        d = time_zone.split('/')
        if len(d) == 2:
            city_name = d[1]
            city_code = city_name[:3].upper()
            city, created = City.objects.get_or_create(name=city_name, code=city_code, timezone=time_zone)
            Airport.objects.get_or_create(name='airport ' + city_name, code=city_code, city=city)
            Airline.objects.get_or_create(name='airline ' + city_name, code=city_code[:2])

    location_airport = Airport.objects.get(name='airport Yekaterinburg')
    for f in range(FLIGHT_NUMBER):
        number = randint(1, 10 ** 4 - 2)
        airline = Airline.objects.order_by('?').first()
        airport = Airport.objects.exclude(id=location_airport.id).order_by('?').first()
        duration = timedelta(hours=randint(0, 30), minutes=randint(0, 60))
        Flight.objects.create(
            number=number,
            airline=airline,
            departure=location_airport,
            arrival=airport,
            duration=duration
        )
        Flight.objects.create(
            number=number+1,
            airline=airline,
            departure=airport,
            arrival=location_airport,
            duration=duration
        )

    for f in Flight.objects.order_by('?'):
        t_delta = timedelta(hours=randint(-70, 70), minutes=randint(0, 60))
        flight, created = ScheduleFlight.objects.get_or_create(
            time_of_departure=timezone.now()+t_delta,
            status=choice(
                [val for val, label in SCHEDULE_FLIGHT_STATUS_CHOICES]
            ),
            flight=f
        )














