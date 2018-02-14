from django.shortcuts import render

# Create your views here.
from flights.models import ScheduleFlight


def flights(request):
    return render(request, 'flights/flight_list.html', {'flights': ScheduleFlight.objects.all()})