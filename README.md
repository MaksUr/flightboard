# Документация.

Для добавления объектов, таких, как города, аэропорты, авиакомпании можно воспользоваться скриптом *\flights\init_data.py*


Для того, чтобы внести изменения в расписание рейсов, можно воспользоваться двумя способами:
*-* интерфейс администратора;
*-* api.

API предоставляет доступ к базе данных сайта для управления рейсами с помощью http-запросов по определеным адресам.
Для создания запросов можно воспользоваться web-интерфейсом или с помощью [httpie](//httpie.org/"httpie"). 
Для доступа необходимо авторизоаваться в интерфейсе администратора.
Для просмотра списка объектов или для добавления нового объекта предусмотрены следующие методы:
*-* */api_scheduleflight_list/* - список всех фактических (которые имеют время вылета) рейсов.
*-* */api_flight_list/* - список рейсов  
*-* */api_city_list/* - список городов  
*-* */api_airport_list/* - список аэропортов  
*-* */api_airline_list/* - список авиакомпаний  

Список методов для редактирования и удаления объектов. {id} - это идентификатор объекта
  

*-* */api_airport/{id}/* - аэропорт  
    **id** - идентификатор объекта  
    **name** - название аэропорта  
    **code** - код IATA  
    **city** - id города  

*-* */api_airline/{id}/* - авиалиния  
    **id** - идентификатор объекта  
    **name** - название авиакомпании  
    **code** - код IATA  

*-* */api_flight/{id}/* - рейс  
    **id** - идентификатор объекта  
    **number** - номер рейса  
    **duration** - продолжительность рейса в формате: [DD][HH:[MM:]]ss.  
    **airline** - id авиакомпании  
    **departure** - id аэропорта отправления  
    **arrival** - id прибытия  

*-* */api_scheduleflight/{id}/* - фактический рейс  
    **id** - идентификатор объекта  
    **time_of_departure** - время вылета, формат: ISO8601 с часовым поясом  
    **status** - статус рейса  
    **flight** - id рейса.  


##Развертывание проекта:
Для развертывания сервера нам необходимо подключиться к удаленому серверу по SSH. Настройку будем производить на сервере Ubuntu 14.04 используя uWSGI и веб-сервер Nginx.

Для начала установим необходимые пакеты :
```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install virtualenv virtualenvwrapper
```
Настроим инициализацию оболочки:
```
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
```
Теперь создадим виртуальное окружения для нашего проекта и активируем его:
```
mkvirtualenv flightboard_env
```
Склонируем наш проект:
```
cd ~
git clone https://github.com/MaksUr/flightboard.git
```
Создадим SECRET_KEY и поместим в папку с проектом:
```
cd ~/flightboard
echo "1j(lfw54!y!f3u%&8%e*(m)@k=p&@2iphm53p$$li&8hy#@gwl" > secret_key.txt
```
Установим зависимости:
```
pip3 install -r requirements.txt
```
Сделаем миграцию, суперпользователя и поместим статичные файлы в специальную директорию:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```
Добавим наш адрес в переменную ALLOWED_HOSTS 
```
nano ~/flightboard/flightboard/settings.py
```
Изменим значение переменной ALLOWED_HOSTS
```
ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . .]
```
При необходимости проинициализируем базу данных значениями аэропортов и городов:
```
cd ~/flightboard
python manage.py shell
>>> from flights.init_data import *
>>> create_airlines() # добавить авиалинии
>>> create_airports() # добавить города и аэропорты
>>> create_flights()  # добавить случайные рейсы
>>> create_schedule_flight()  # добавить фактические случайные рейсы
```
Проверим, работает ли наш проект:
```
python manage.py runserver
```
Перейдем по адресу http://server_domain_or_IP:8080
Если все в порядке и сайт работает, то продолжаем:
Выйдем из локального окружения:
```
deactivate
```
##Установка uWSGI
```
sudo apt-get install python3-dev
sudo pip3 install uwsgi
uwsgi --http :8080 --home /home/user/Env/flightboard_env --chdir /home/user/flightboard -w flightboard.wsgi
```
Если сайт доступен по адресу, продолжаем. Создадим конфигурационные файлы:
```
sudo mkdir -p /etc/uwsgi/sites
cd /etc/uwsgi/sites
sudo nano flightboard.ini
```
Добавим текст в файл flightboard.ini:
```
[uwsgi]
project = flightboard
base = /home/user

chdir = %(base)/%(project)
home = %(base)/Env/%(project)
module = %(project).wsgi:application

master = true
processes = 5

socket = %(base)/%(project)/%(project).sock
chmod-socket = 664
vacuum = true
```
Настроим автоматический запуск uWSGI:
```
sudo nano /etc/init/uwsgi.conf
```
Добавим в файл uwsgi.conf:
```
description "uWSGI application server in Emperor mode"

start on runlevel [2345]
stop on runlevel [!2345]

setuid user
setgid www-data

exec /usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
```
##Настройка Nginx и прокси
Установим Nginx
```
sudo apt-get install nginx
```
Настроим конфигурацию:
```
sudo nano /etc/nginx/sites-available/flightboard
```
Добавим текст (sitenameflightboard - адрес нашего сервера):
```
server {
    listen 80;
    server_name sitenameflightboard.com www.sitenameflightboard.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user/flightboard;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/home/user/flightboard/flightboard.sock;
    }
}
```
Создадим симлинк на конфиг:
```
sudo ln -s /etc/nginx/sites-available/flightboard /etc/nginx/sites-enabled
sudo service nginx configtest
```
Если ошибок не обнаружено:
```
sudo service nginx restart
sudo service uwsgi start
```
Если при зоходе на сайт появляется страница привествия Nginx, то необходимо выполнить:
```
sudo rm -v /etc/nginx/sites-enabled/default
sudo service nginx restart
```