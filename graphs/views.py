import time
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from household.models import Household
from meter.models import MeterType
from meter.models import MeterReading


def get_meter_values(request, household, meter):
    ret_values = {}
    ret_values['key'] = "Quantity"
    ret_values['bar'] = True
    vals = []
    hh = int(household)
    mt = int(meter)
    hh_rec = Household.objects.get(id=hh)
    m_rec = MeterType.objects.get(id=mt)
    val_rec = MeterReading.objects.filter(household=hh_rec, meter_type=m_rec)
    for rec in val_rec:
        srec = []
        srec.append(int(time.mktime(rec.ts.timetuple())*1000))
        srec.append(rec.meter_reading)
        # srec = [ 1164862800000 , 389.0]
        vals.append(srec)
        print (rec)
    ret_values['values'] = vals
    result = [ret_values]
    return JsonResponse(result, safe=False)


def graph_home(request, household, meter):
    hh = int(household)
    mt = int(meter)
    hh_rec = Household.objects.get(id=hh)
    m_rec = MeterType.objects.get(id=mt)
    val_rec = MeterReading.objects.filter(household=hh_rec, meter_type=m_rec)
    for rec in val_rec:
        print (rec)
    info = {"household": household, "meter": meter}
    return render_to_response("consumption_client.html", info, RequestContext(request))
