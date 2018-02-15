import django_tables2 as tables

from flights.models import ScheduleFlight


class ScheduleFlightTable(tables.Table):
    arrival_status = tables.Column()
    arrival_time = tables.Column()
    duration = tables.Column(accessor='flight.duration')

    class Meta:
        model = ScheduleFlight
        # fields = ['time_of_departure', 'duration', 'arrival_time']

