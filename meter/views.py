import json
import datetime
import time
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from household.models import MetertypeHousehold
from meter.models import MeterReading
from meter.models import MeterType
from django.utils import timezone
from django.utils.timezone import localtime
from household.models import UserHousehold


def get_meter_types(request):
    meter_info = {'result': True}
    user = User.objects.get(username=request.user)
    try:
        household_rec = UserHousehold.objects.get(user=user)
        household = household_rec.household
    except Exception as e:
        print (e)
        return meter_info
    meter_types_household = MetertypeHousehold.objects.filter(household=household)
    meter_list = []
    for meter_type_household in meter_types_household:
        meter_rec = {}
        meter_rec['value'] = meter_type_household.id
        meter_rec['displayName'] = meter_type_household.meter_type.name
        meter_rec['wholeText'] = meter_type_household.meter_type.color_whole
        meter_rec['fragText'] = meter_type_household.meter_type.color_fraction
        print ("photo", meter_type_household.meter_type.photo)
        if meter_type_household.meter_type.photo != "":
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
            household_rec = UserHousehold.objects.get(user=user)
            household = household_rec.household
        except Exception as e:
            print (e)
            r['reason'] = "not connected to household"
            return r

        meter_reading = MeterReading()
        meter_reading.meter_register = user
        meter_type_household = MetertypeHousehold.objects.get(id=data['id'])
        meter_type = meter_type_household.meter_type
        meter_reading.meter_type = meter_type
        meter_reading.household = household
        try:
            meter_r = str(data['meterWhole']) + "." + data['meterFrag']
            meter_reading.meter_reading = float(meter_r)
        except Exception as e:
            print (e)
            r['reason'] = "Meter reading not correct"
            return r

        try:
            dt = datetime.datetime(
                            year=data['meterJaar'], month=data['meterMaand'], day=data['meterDag'],
                            minute=data['meterMinuten'], hour=data['meterUur'])
        except Exception as e:
            print (e)
            r['reason'] = "Timestamp not correct"
            return r

        meter_reading.ts = dt
        try:
            meter_reading.save()
        except Exception as e:
            print (e)
            r['reason'] = "Save failed, only 1 reading for a given timestamp"
            return r

        r['result'] = True
        # validate now the content
        r['meterWhole'] = 0
        r['meterFrag'] = '0'
    else:
        r['reason'] = "Hmm, contact your admin"
        r = {'result': False}
    return JsonResponse(r, safe=False)


def get_meter_readings(request):
    meter_info = {'result': True}
    user = User.objects.get(username=request.user)
    try:
        household_rec = UserHousehold.objects.get(user=user)
        household = household_rec.household
    except Exception as e:
        print (e)
        meter_info['result'] = False
        return
    meter_readings = MeterReading.objects.filter(household=household).order_by('-ts')
    meter_list = []
    for meter_reading in meter_readings:
        rec = {}
        dt = localtime(meter_reading.ts)
        rec['time'] = dt.strftime('%d %b %Y %H:%M')
        rec['meter_type'] = str(meter_reading.meter_type.name)
        rec['meter_reading'] = str(meter_reading.meter_reading)
        rec['meter_register'] = \
            str(meter_reading.meter_register.first_name) + " " +\
            str(meter_reading.meter_register.last_name)
        meter_list.append(rec)

    return JsonResponse(meter_list, safe=False)
