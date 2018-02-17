import django_filters
from django_filters import FilterSet

from flights.models import ScheduleFlight


class FlightFilter(FilterSet):
    airline = django_filters.CharFilter(name='flight__airline__code', lookup_expr='icontains', label='Код авиакомпании')
    flight_number = django_filters.NumberFilter(name='flight__number', lookup_expr='icontains', label='Номер рейса')

    class Meta:
        model = ScheduleFlight
        fields = ['airline', 'flight_number',]

    def __init__(self, data=None, queryset=None, prefix=None, strict=None, request=None):
        super().__init__(data=data, queryset=queryset, prefix=prefix, strict=strict, request=request)

