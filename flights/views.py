from django.utils import timezone
from django_filters.views import FilterView
from django_tables2 import SingleTableView, SingleTableMixin

# Create your views here.
from flights.filters import FlightFilter, flight_queryset
from flights.models import ScheduleFlight
from flights.tables import ScheduleFlightTable


class FlightList(SingleTableMixin, FilterView):
    model = ScheduleFlight
    table_class = ScheduleFlightTable
    template_name = 'flights/flight_list.html'
    filterset_class = FlightFilter
    queryset = flight_queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
