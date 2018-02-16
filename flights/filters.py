from django_filters import FilterSet

from flights.models import ScheduleFlight


class FlightFilter(FilterSet):

    class Meta:
        model = ScheduleFlight
