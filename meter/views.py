import json
import datetime
import time
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from gezin.models import MeterTypeHousehold
from meter.models import MeterReading
from meter.models import MeterType
from django.utils import timezone
from django.utils.timezone import localtime
from household.models import UserHousehold


def testje(request):
    return render_to_response("enter_meter.html", {}, RequestContext(request))


def get_meter_types(request):
    meter_info = {'result': True}
    user = User.objects.get(username=request.user)
    try:
        household_rec = UserHousehold.objects.get(user=user)
        household = household_rec.household
    except Exception as e:
        print (e)
        return meter_info
    meter_types_household = MeterTypeHouseHold.objects.filter(household=household)
    meter_list = []
    for meter_type_household in meter_types_household:
        meter_rec = {}
        meter_rec['value'] = meter_type_household.id
        meter_rec['displayName'] = meter_type_household.meter_type.name
        meter_rec['wholeText'] = meter_type_household.meter_type.color_whole
        meter_rec['fragText'] = meter_type_household.meter_type.color_fraction
        print ("photo", meter_type_household.meter_type.photo)
        if meter_type_gezin.meter_type.photo != "":
            meter_rec['picture'] = meter_type_household.meter_type.photo.url
        else:
            meter_rec['picture'] = '/static/theme/img/icon_meter.png'
        meter_list.append(meter_rec)
    now = time.localtime(time.time())
    current_time = {}
    current_time['year'] = now.tm_year
    current_time['month'] = now.tm_mon
    current_time['day'] = now.tm_mday
    current_time['hour'] = now.tm_hour
    current_time['minute'] = now.tm_min
    meter_info['meter_types'] = meter_list
    meter_info['current_time'] = current_time

    return JsonResponse(meter_info, safe=False)


def save_meter(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        print ("data", data, type(data))
        print (data['id'])
        r = data
        r['result'] = False

        user = User.objects.get(username=request.user)
        try:
            household_rec = UserHouseHold.objects.get(user=user)
            household = household_rec.household
        except Exception as e:
            print (e)
            r['reason'] = "not connected to household"
            return r

        meter_reading = MeterReading()
        meter_reading.opnemer = user
        meter_type_household = MeterTypeHousehold.objects.get(id=data['id'])
        meter_type = meter_type_household.meter_type
        meter_reading.meter_type = meter_type
        meter_reading.household = household
        try:
            stand = str(data['meterWhole']) + "." + data['meterFrag']
            meter_reading.stand = float(stand)
        except Exception as e:
            print (e)
            r['reason'] = "Ingave meterstand is niet correct, pas aan aub"
            return r

        try:
            dt = datetime.datetime(
                            year=data['meterJaar'], month=data['meterMaand'], day=data['meterDag'],
                            minute=data['meterMinuten'], hour=data['meterUur'])
        except Exception as e:
            print (e)
            r['reason'] = "Ingave tijd is niet correct, pas aan aub"
            return r

        meter_stand.tijdstip = dt
        try:
            meter_stand.save()
            print ("weggeschreven")
        except Exception as e:
            print (e)
            r['reason'] = "Wegschrijven mislukt, graag 1 stand per tijdstip en meter type"
            return r

        r['result'] = True
        # validate now the content
        r['meterWhole'] = 0
        r['meterFrag'] = '0'
    else:
        r['reason'] = "Hmm, contacteer je energiemeester"
        r = {'result': False}
    return JsonResponse(r, safe=False)


def get_meter_standen(request):
    meter_info = {'result': True}
    user = User.objects.get(username=request.user)
    try:
        gezin_rec = GebruikerGezin.objects.get(user=user)
        gezin = gezin_rec.gezin
    except Exception as e:
        print (e)
        meter_info['result'] = False
        return
    meter_stands = MeterStand.objects.filter(gezin=gezin).order_by('-tijdstip')
    meter_list = []
    for meter_stand in meter_stands:
        rec = {}
        dt = localtime(meter_stand.tijdstip)
        rec['time'] = dt.strftime('%d %b %Y %H:%M')
        rec['meter_type'] = str(meter_stand.meter_type)
        rec['meter_stand'] = str(meter_stand.stand)
        rec['opnemer'] = str(meter_stand.opnemer.first_name) + " " + str(meter_stand.opnemer.last_name)
        meter_list.append(rec)

    return JsonResponse(meter_list, safe=False)
