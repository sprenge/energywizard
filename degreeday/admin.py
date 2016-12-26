from django.contrib import admin

from .models import DegreedaySource
from .models import Degreeday

class DegreedayAdmin(admin.ModelAdmin):
    list_display = ['source', 'date_day', 'value']

admin.site.register(DegreedaySource)
admin.site.register(Degreeday, DegreedayAdmin)
