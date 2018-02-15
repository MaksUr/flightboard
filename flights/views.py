from django.shortcuts import render
from django_tables2 import RequestConfig


# Create your views here.
from django.utils import timezone

from flights.models import ScheduleFlight
from flights.tables import ScheduleFlightTable


def flights(request):
    table = ScheduleFlightTable(ScheduleFlight.objects.all())
    RequestConfig(request).configure(table)
    return render(
        request,
        'flights/flight_list.html', {
            'flights': table,
            'now': timezone.now(),
        }
    )