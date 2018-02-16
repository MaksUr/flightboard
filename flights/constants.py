AIRPORT_LOCATION = 'SVO'
# model City
CITY_VERBOSE_NAME = 'Город'
CITY_VERBOSE_NAME_PLURAL = 'Города'
# name
CITY_NAME = 'name'
CITY_NAME_KEY = 'Название города'
CITY_NAME_HELP = ''
# country_code
CITY_COUNTRY_CODE = 'country_code'
CITY_COUNTRY_CODE_KEY = 'Код страны'
CITY_COUNTRY_CODE_HELP = 'Состоит из 2 букв.'
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
# departure
FLIGHT_DEPARTURE = 'departure'
FLIGHT_DEPARTURE_KEY = 'Аэропорт вылета'
FLIGHT_DEPARTURE_HELP = ''
# arrival
FLIGHT_ARRIVAL = 'arrival'
FLIGHT_ARRIVAL_KEY = 'Аэропорт прибытия'
FLIGHT_ARRIVAL_HELP = ''
# duration
FLIGHT_DURATION = 'duration'
FLIGHT_DURATION_KEY = 'В пути'
FLIGHT_DURATION_HELP = 'Используйте формат D HH:MM:SS, где D - количество дней, H - часов, M - минут, S - секунд.'

# model ScheduleFlight
SCHEDULE_FLIGHT_VERBOSE_NAME = 'Фактический рейс'
SCHEDULE_FLIGHT_VERBOSE_NAME_PLURAL = 'Фактические рейсы'
# time_of_departure
SCHEDULE_FLIGHT_TIME_OF_DEPARTURE = 'time_of_departure'
SCHEDULE_FLIGHT_TIME_OF_DEPARTURE_KEY = 'Время вылета.'
SCHEDULE_FLIGHT_TIME_OF_DEPARTURE_HELP = 'Время прилета высчитывается автоматически исходя из продолжительности рейса.'
SCHEDULE_FLIGHT_STATUS_CHOICES = (
    ('flying', 'В полете'),
    ('arrive', 'Прибыл'),
    ('registration', 'Регистрация'),
)
# time_of_arrival
SCHEDULE_FLIGHT_TIME_OF_ARRIVAL = 'time_of_arrival'
SCHEDULE_FLIGHT_TIME_OF_ARRIVAL_KEY = 'Фактическое местное время прибытия.'
SCHEDULE_FLIGHT_TIME_OF_ARRIVAL_HELP = ''
# status
SCHEDULE_FLIGHT_STATUS = 'status'
SCHEDULE_FLIGHT_STATUS_KEY = 'Статус рейса.'
SCHEDULE_FLIGHT_STATUS_HELP = ''
# flight
SCHEDULE_FLIGHT_FLIGHT = 'flight'
SCHEDULE_FLIGHT_FLIGHT_KEY = 'Рейс'
SCHEDULE_FLIGHT_FLIGHT_HELP = 'Если необходимый рейс отсутствует, то его необходимо добавить.'
