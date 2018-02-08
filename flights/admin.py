from django.contrib import admin

# Register your models here.
from flights.forms import CityForm, AirportForm, AirlineForm, FlightForm
from flights.models import City, Airport, Airline, Flight


class AdminCity(admin.ModelAdmin):
    form = CityForm
admin.site.register(City, AdminCity)


class AdminAirport(admin.ModelAdmin):
    form = AirportForm
admin.site.register(Airport, AdminAirport)


class AdminAirline(admin.ModelAdmin):
    form = AirlineForm
admin.site.register(Airline, AdminAirline)


class AdminFlight(admin.ModelAdmin):
    form = FlightForm
admin.site.register(Flight, AdminFlight)
