import datetime
from django.core.management.base import BaseCommand, CommandError
import requests
import pandas
from lxml import html
from degreeday.models import DegreedaySource
from degreeday.models import Degreeday


base_link = "http://www.aardgas.be"


class Command(BaseCommand):
    help = 'Import dagelijkse graaddagen from http://www.aardgas.be/nl/particulier/graaddagen'

    def handle(self, *args, **options):
        r = requests.get(base_link+'/nl/particulier/graaddagen')
        tree = html.fromstring(r.content)
        e = tree.xpath('.//a[contains(text(),"Dagelijkse gegevens")]')
        df = pandas.read_excel(base_link+e[0].attrib['href'])
        for r in df.iterrows():
            r1 = r[1][0]
            r2 = r[1][1]
            if isinstance(r1, datetime.datetime):
                d = r1.date()
                print(d, r2)
                dds = DegreedaySource.objects.get(name="aardgas")
                print (r2)
                dd = Degreeday()
                dd.source = dds
                dd.date_day = d
                dd.value = r2
                try:
                    dd.save()
                except Exception as e:
                    print (e)
