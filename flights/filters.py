import django_filters
from django_filters import FilterSet

from flights.models import ScheduleFlight, Airline, Flight, Airport

flight_queryset = ScheduleFlight.objects.all()


def get_airline_queryset(request):
    return Airline.objects.filter(flight__scheduleflight__in=flight_queryset).distinct()


def get_flight_number_queryset(request):
    return Flight.objects.filter(scheduleflight__in=flight_queryset)


def get_departure_queryset(request):
    return Airport.objects.filter(airport_dep__scheduleflight__in=flight_queryset).distinct()


def get_arrival_queryset(request):
    return Airport.objects.filter(airport_arr__scheduleflight__in=flight_queryset).distinct()


class FlightFilter(FilterSet):
    airline = django_filters.ModelChoiceFilter(name='flight__airline', label='Код авиакомпании', queryset=get_airline_queryset)
    flight_number = django_filters.ModelChoiceFilter(name='flight', label='Рейс', queryset=get_flight_number_queryset)
    departure = django_filters.ModelChoiceFilter(name='flight__departure', label='Отправление', queryset=get_departure_queryset)
    arrival = django_filters.ModelChoiceFilter(name='flight__arrival', label='Прибытие', queryset=get_arrival_queryset)

    class Meta:
        model = ScheduleFlight
        fields = ['airline', 'flight_number', 'departure', 'status']

    def __init__(self, data=None, queryset=None, prefix=None, strict=None, request=None):
        super().__init__(data=data, queryset=queryset, prefix=prefix, strict=strict, request=request)

