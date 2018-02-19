from django.utils import six
from rest_framework import serializers

from flights.models import City, Airport, Airline, Flight, ScheduleFlight


class CitySerializer(serializers.ModelSerializer):
    timezone = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = '__all__'

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class ScheduleFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleFlight
        fields = [
            "id",
            "time_of_departure",
            "status",
            "flight",
        ]

