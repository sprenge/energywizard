from django.contrib import admin

from .models import Household
from .models import MetertypeHousehold
from .models import UserHousehold

admin.site.register(Household)
admin.site.register(MetertypeHousehold)
admin.site.register(UserHousehold)
