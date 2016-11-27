from django.db import models
from django.contrib.auth.models import User, Group
from django_countries.fields import CountryField
from degreeday.models import DegreedaySource


class Household(models.Model):
    name = models.CharField('name household', max_length=128, blank=True)
    nbr_members = models.IntegerField("number of members in household", default=1)
    address = models.CharField('street and number', max_length=256, blank=True)
    phone = models.CharField('phone number', max_length=64, blank=True)
    postal_code = models.CharField('postal code', max_length=32)
    city = models.CharField('city', max_length=128, blank=True)
    country = CountryField('country')
    info = models.TextField('info', blank=True, null=True)
    active = models.BooleanField("guided at this moment", default=True)
    degreeday_source = models.ForeignKey(DegreedaySource, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)+"_"+str(postal_code)

    def __str__(self):
        return str(self.name)+"_"+str(postal_code)

    class Meta:
        verbose_name_plural = "Households"


class MetertypeHousehold(models.Model):
    household = models.ForeignKey(Household)
    meter_type = models.ForeignKey("meter.MeterType")
    meter_id = models.CharField('meter id', max_length=128, blank=True)
    order = models.IntegerField("order, high=more important", default=0)

    def __unicode__(self):
        return str(self.household) + "_" + str(self.meter_type)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name_plural = "MeterTypesHouseholds"
        unique_together = ('household', 'meter_type')


class UserHousehold(models.Model):
    '''
    Table binds a user account to a household
    '''
    household = models.ForeignKey(Household)
    user = models.OneToOneField(User, unique=True)

    def __unicode__(self):
        return str(self.household) + "_" + str(self.user)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name_plural = "UsersHouseholds"
