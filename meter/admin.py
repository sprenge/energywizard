from django.contrib import admin
from import_export import resources
from .models import EnergieType
from .models import MeterType
from .models import MeterReading
from import_export.admin import ImportExportModelAdmin


class ReadingResource(resources.ModelResource):

    class Meta:
        model = MeterReading

class MeterReadingAdmin(ImportExportModelAdmin):
    resource_class = ReadingResource


class EnergyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_device')
    list_filter = ('is_device',)

admin.site.register(EnergieType)
admin.site.register(MeterType, EnergyTypeAdmin)
admin.site.register(MeterReading, MeterReadingAdmin)
