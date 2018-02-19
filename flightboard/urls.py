"""flightboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from flights.views import ArriveFlightList, DepartFlightList, CityDetail, AirportDetail, AirlineDetail, FlightDetail, \
    ScheduleFlightDetail, ScheduleFlightList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ArriveFlightList.as_view(), name='arrive'),
    url(r'^depart/$', DepartFlightList.as_view(), name='depart'),
    url(r'^api_city/(?P<pk>([0-9]+))/$', CityDetail.as_view(), name='api_city'),
    url(r'^api_airport/(?P<pk>([0-9]+))/$', AirportDetail.as_view(), name='api_airport'),
    url(r'^api_airline/(?P<pk>([0-9]+))/$', AirlineDetail.as_view(), name='api_airline'),
    url(r'^api_flight/(?P<pk>([0-9]+))/$', FlightDetail.as_view(), name='api_flight'),
    url(r'^api_scheduleflight/(?P<pk>([0-9]+))/$', ScheduleFlightDetail.as_view(), name='api_schedule_flight'),
    url(r'^api_scheduleflight_list/$', ScheduleFlightList.as_view(), name='api_schedule_flights'),
]
