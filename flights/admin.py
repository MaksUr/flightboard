from django.contrib import admin

# Register your models here.
from flights.models import City, Airport, Airline, Flight


class AdminCity(admin.ModelAdmin):
    pass
admin.site.register(City, AdminCity)


class AdminAirport(admin.ModelAdmin):
    pass
admin.site.register(Airport, AdminAirport)


class AdminAirline(admin.ModelAdmin):
    pass
admin.site.register(Airline, AdminAirline)


class AdminFlight(admin.ModelAdmin):
    pass
admin.site.register(Flight, AdminFlight)
