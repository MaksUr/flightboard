from django.db import models

# Create your models here.
from django.db.models import CharField

from flights.constants import FLIGHT_NUMBER_KEY


class Flight(models.Model):
    number = CharField(FLIGHT_NUMBER_KEY, max_length=8, validators=[])