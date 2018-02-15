import django_tables2 as tables

from flights.models import ScheduleFlight


class ScheduleFlightTable(tables.Table):
    arrival_status = tables.Column()
    duration = tables.Column(accessor='flight.duration')

    class Meta:
        model = ScheduleFlight

    def order_arrival_status(self, queryset, is_descending):
        queryset = queryset.annotate().order_by(('-' if is_descending else '') + 'time_of_arrival')
        return queryset, True
