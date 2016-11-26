from django.contrib import admin

from .models import Household
from .models import MeterTypeHousehold
from .models import UserHousehold

admin.site.register(Household)
admin.site.register(MeterTypeHousehold)
admin.site.register(UserHousehold)
