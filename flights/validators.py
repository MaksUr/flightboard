import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

FLIGHT_NUMBER_PATTERN = re.compile(r'^([\w][\w]|[\w][\d]|[\w])?[\d]{1,4}[\d]?$', re.IGNORECASE)


def flight_number_validate(flight_number):
    # TODO: add tests
    """

    :rtype: str
    :type flight_number: str
     
    """
    m = re.match(FLIGHT_NUMBER_PATTERN, flight_number)
    if m is None:
        raise ValidationError(
            _('Номер рейса: "{flight_number}" имеет неверный формат. Примеры: "DP259", "S767888", "S7 55"'),
            params={'flight_number': flight_number},
        )
