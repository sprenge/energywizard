from django.db import models
from household.models import Household
from django.contrib.auth.models import User, Group


class EnergieType(models.Model):
    name = models.CharField("energie type", max_length=256, help_text="e.g. Gas, Water", unique=True)
    e_unit = models.CharField("energy unit", max_length=128, help_text="e.g. KW")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name_plural = "EnergieTypes"


class MeterType(models.Model):
    name = models.CharField("meter type", max_length=256, help_text="e.g. day counter elektricity")
    variant = models.CharField("variant", default="standard", max_length=256)
    color_whole = models.CharField(
                        "color whole meter part",
                        default="White digits on black blackground",
                        max_length=128)
    max_whole = models.IntegerField("maximum number of figures whole meter part", default=6)
    color_fraction = models.CharField(
                        "Color fraction figure",
                        default="White digits on black blackground",
                        max_length=128, blank=True, null=True)
    max_fraction = models.IntegerField("maximum number of figures fraction part", default=4)  # 0 is disabled
    photo = models.ImageField("photo meter (200x200)", blank=True, null=True)
    energie_type = models.ForeignKey(EnergieType)
    is_device = models.BooleanField("is a device", default=False)

    def __unicode__(self):
        return str(self.name)+"_"+str(self.variant)

    def __str__(self):
        return self.__unicode__()


class MeterReading(models.Model):
    meter_register = models.ForeignKey(User)
    meter_type = models.ForeignKey(MeterType)
    household = models.ForeignKey(Household)
    meter_reading = models.FloatField("meter reading")
    ts = models.DateTimeField("timestamp measurement")

    def __unicode__(self):
        return str(self.household) + "_" + str(self.meter_type) + "_" + str(self.ts) + "_" + str(self.meter_reading)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        unique_together = ('ts', 'household', 'meter_type')
