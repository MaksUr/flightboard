
# model City
CITY_VERBOSE_NAME = 'Город'
CITY_VERBOSE_NAME_PLURAL = 'Города'
# name
CITY_NAME = 'name'
CITY_NAME_KEY = 'Название города'
CITY_NAME_HELP = ''
# code
CITY_CODE = 'code'
CITY_CODE_KEY = 'Код города'
CITY_CODE_HELP = 'Должен соответсвовать коду IATA. Состоит из 3 букв.'
# timezone
CITY_TIMEZONE = 'timezone'
CITY_TIMEZONE_KEY = 'Часовой пояс'
CITY_TIMEZONE_HELP = ''

# model Airport
AIRPORT_VERBOSE_NAME = 'Aэропорт'
AIRPORT_VERBOSE_NAME_PLURAL = 'Aэропорты'
# name
AIRPORT_NAME = 'name'
AIRPORT_NAME_KEY = 'Название аэропорта'
AIRPORT_NAME_HELP = ''
# code
AIRPORT_CODE = 'code'
AIRPORT_CODE_KEY = 'Код аэропорта'
AIRPORT_CODE_HELP = 'Должен соответсвовать коду IATA. Состоит из 3 букв.'
# city
AIRPORT_CITY = 'city'
AIRPORT_CITY_KEY = CITY_VERBOSE_NAME
AIRPORT_CITY_HELP = ''

# model Airline
AIRLINE_VERBOSE_NAME = 'Авиалиния'
AIRLINE_VERBOSE_NAME_PLURAL = 'Авиалинии'
# name
AIRLINE_NAME = 'name'
AIRLINE_NAME_KEY = 'Авиакомпания'
AIRLINE_NAME_HELP = ''
# code
AIRLINE_CODE = 'code'
AIRLINE_CODE_KEY = 'Код авиакомпании'
AIRLINE_CODE_HELP = 'Должен соответсвовать коду IATA. Состоит из 3 букв.'

# model Flight
FLIGHT_VERBOSE_NAME = 'Рейс'
FLIGHT_VERBOSE_NAME_PLURAL = 'Рейсы'
# number
FLIGHT_NUMBER = 'number'
FLIGHT_NUMBER_KEY = 'Номер рейса'
FLIGHT_NUMBER_HELP = 'Состоит из цифр, не более четырех.'
# airline
FLIGHT_AIRLINE = 'airline'
FLIGHT_AIRLINE_KEY = AIRLINE_VERBOSE_NAME
FLIGHT_AIRLINE_HELP = ''


