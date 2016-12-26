from django.core.management.base import BaseCommand, CommandError
import requests
import pandas
import datetime
from degreeday.models import DegreedaySource
from degreeday.models import Degreeday


ilist = [
        'http://www.aardgas.be/sites/default/files/sites/default/files/imce/DJE01new-1.xls',
        ]


class Command(BaseCommand):
    help = 'Import graaddagen from http://www.aardgas.be/nl/particulier/graaddagen'

    def handle(self, *args, **options):
        for xls in ilist:
            df = pandas.read_excel(xls)
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
                    dd.save()
