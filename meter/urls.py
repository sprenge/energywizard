from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^save_meter$',
        views.save_meter,
        name='save_meter'),
    url(
        r'^get_meter_types$',
        views.get_meter_types,
        name='get_meter_types'),
    url(
        r'^get_meter_readings$',
        views.get_meter_readings,
        name='get_meter_readings'),
]
