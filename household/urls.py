from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^getall$',
        views.get_all_households,
        name='get_all_households'),
    url(
        r'^save_household_user$',
        views.save_household_user,
        name='save_household_user'),
]
