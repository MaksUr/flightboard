from django.utils import timezone
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

# Create your views here.
from flights.constants import LOCATION_AIRPORT_CODE, SCHEDULE_FLIGHT_TIME_OF_DEPARTURE, SCHEDULE_FLIGHT_TIME_OF_ARRIVAL
from flights.filters import FlightFilter
from flights.models import ScheduleFlight
from flights.tables import ScheduleFlightTable


class FlightList(SingleTableMixin, FilterView):
    model = ScheduleFlight
    table_class = ScheduleFlightTable
    template_name = 'flights/flight_list.html'
    filterset_class = FlightFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['flight_count'] = len(self.object_list)
        return context


class DepartFlightList(FlightList):
    queryset = ScheduleFlight.objects.filter(
    flight__departure__code=LOCATION_AIRPORT_CODE).order_by(SCHEDULE_FLIGHT_TIME_OF_DEPARTURE)


class ArriveFlightList(FlightList):
    queryset = ScheduleFlight.objects.filter(
    flight__arrival__code=LOCATION_AIRPORT_CODE).order_by(SCHEDULE_FLIGHT_TIME_OF_ARRIVAL)
