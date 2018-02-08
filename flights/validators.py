import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

PATTERN_CODE = re.compile(r'^([A-Z]){3}$', re.IGNORECASE)
CODE_ERROR_MESSAGE = '"{code}" - имеет неверное значение. Код должен состоять из трех букв.'

PATTERN_AIRLINE_CODE = re.compile(r'^([A-Z\d]){2}$', re.IGNORECASE)
CODE_AIRLINE_ERROR_MESSAGE = '"{code}" - имеет неверное значение. Код авиакомпаниидолжен состоять из 2 символов.'


def code_validate(code):
    """

    :type code: str
    """
    m = re.match(PATTERN_CODE, code)
    if m is None:
        raise ValidationError(_(CODE_ERROR_MESSAGE), params={'code': code},)


def city_code_validate(city_code):
    """

    :type city_code: str
    """
    # TODO: add link to specification
    code_validate(city_code)


def airport_code_validate(airport_code):
    """

    :type airport_code: str
    """
    # TODO: add link to specification
    code_validate(airport_code)


def airline_code_validate(airline_code):
    """

    :type airline_code: str
    """
    m = re.match(PATTERN_AIRLINE_CODE, airline_code)
    if m is None:
        raise ValidationError(_(CODE_ERROR_MESSAGE), params={'code': airline_code},)


def flight_number_validate(flight_number):
    # TODO: add link to wikipedia (limit flight numbers to four digits)
    """
    :type flight_number: int
     
    """
    if (flight_number <= 0) or (flight_number >= 10**4):
        raise ValidationError(
            _('Номер рейса: "{flight_number}" имеет неверное значение. '
              'Номер включает число, состоящее не более чем из 4 цифр.'),
            params={'flight_number': flight_number},
        )
