from django.forms import ModelForm

from flights.constants import CITY_NAME, CITY_CODE, CITY_TIMEZONE, AIRPORT_NAME, AIRPORT_CODE, AIRPORT_CITY, \
    AIRLINE_NAME, AIRLINE_CODE, FLIGHT_NUMBER, FLIGHT_AIRLINE, CITY_NAME_HELP, CITY_CODE_HELP, CITY_TIMEZONE_HELP, \
    AIRPORT_NAME_HELP, AIRPORT_CODE_HELP, AIRPORT_CITY_HELP, AIRLINE_NAME_HELP, AIRLINE_CODE_HELP, FLIGHT_NUMBER_HELP, \
    FLIGHT_AIRLINE_HELP, FLIGHT_DEPARTURE, FLIGHT_ARRIVAL, FLIGHT_DURATION, FLIGHT_DEPARTURE_HELP, FLIGHT_ARRIVAL_HELP, \
    FLIGHT_DURATION_HELP
from flights.models import City, Airport, Airline, Flight


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = [
            CITY_NAME,
            CITY_CODE,
            CITY_TIMEZONE,
        ]
        help_texts = {
            CITY_NAME: CITY_NAME_HELP,
            CITY_CODE: CITY_CODE_HELP,
            CITY_TIMEZONE: CITY_TIMEZONE_HELP,
        }


class AirportForm(ModelForm):
    class Meta:
        model = Airport
        fields = [
            AIRPORT_NAME,
            AIRPORT_CODE,
            AIRPORT_CITY,
        ]
        help_texts = {
            AIRPORT_NAME: AIRPORT_NAME_HELP,
            AIRPORT_CODE: AIRPORT_CODE_HELP,
            AIRPORT_CITY: AIRPORT_CITY_HELP,
        }


class AirlineForm(ModelForm):
    class Meta:
        model = Airline
        fields = [
            AIRLINE_NAME,
            AIRLINE_CODE,
        ]
        help_texts = {
            AIRLINE_NAME: AIRLINE_NAME_HELP,
            AIRLINE_CODE: AIRLINE_CODE_HELP,
        }


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = [
            FLIGHT_NUMBER,
            FLIGHT_AIRLINE,
            FLIGHT_DEPARTURE,
            FLIGHT_ARRIVAL,
            FLIGHT_DURATION,
        ]
        help_texts = {
            FLIGHT_NUMBER: FLIGHT_NUMBER_HELP,
            FLIGHT_AIRLINE: FLIGHT_AIRLINE_HELP,
            FLIGHT_DEPARTURE: FLIGHT_DEPARTURE_HELP,
            FLIGHT_ARRIVAL: FLIGHT_ARRIVAL_HELP,
            FLIGHT_DURATION: FLIGHT_DURATION_HELP,
        }
