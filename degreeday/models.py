from django.db import models


class DegreedaySource(models.Model):
    name = models.CharField('name source degree day', max_length=512, unique=True)
    api_key = models.CharField('api key', max_length=512, blank=True)
    api_secret = models.CharField('api key', max_length=512, blank=True)
    base_temperature = models.FloatField(default='16.5')
    station_id = models.CharField('wether station id', max_length=512, blank=True)
    fetch_url = models.CharField('nase url for fetching info', max_length=1024, blank=True)
    fetch_method = models.CharField('how to fetch data', max_length=512, default='aardgas.be')

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return self.__unicode__()


class Degreeday(models.Model):
    source = models.ForeignKey(DegreedaySource)
    date_day = models.DateField()
    value = models.FloatField()

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        unique_together = ('source', 'date_day', 'value')