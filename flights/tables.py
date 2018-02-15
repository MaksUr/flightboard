import django_tables2 as tables

from flights.models import ScheduleFlight


class AirportColumn(tables.Column):
    def render(self, value):
        return value.info


class ScheduleFlightTable(tables.Table):
    arrival_status = tables.Column(verbose_name='Прибытие')
    duration = tables.Column(accessor='flight.duration')
    departure = AirportColumn(accessor='flight.departure')
    arrival = AirportColumn(accessor='flight.arrival')

    class Meta:
        model = ScheduleFlight
        fields = ['flight', 'departure', 'time_of_departure', 'duration', 'time_of_arrival', 'arrival', 'status', 'arrival_status']

    def render_arrival_status(self, value):
        if value:
            return 'Прибыл'
        else:
            return 'В пути'

    def render_flight(self, value):
        return value.codename()

    def order_arrival_status(self, queryset, is_descending):
        queryset = queryset.order_by(('-' if is_descending else '') + 'time_of_arrival')
        return queryset, True

    def order_flight(self, queryset, is_descending):
        queryset = queryset.order_by(
            ('-' if is_descending else '') + 'flight__airline__code',
            ('-' if is_descending else '') + 'flight__number'
        )
        return queryset, True
