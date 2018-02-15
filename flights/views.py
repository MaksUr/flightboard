from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from flights.models import ScheduleFlight
from flights.tables import ScheduleFlightTable


def flights(request):
    return render(
        request,
        'flights/flight_list.html', {
            'flights': ScheduleFlightTable(ScheduleFlight.objects.all()),
            'now': timezone.now(),
            # 'simple_table': SimpleTable(simple_table_data)
        }
    )