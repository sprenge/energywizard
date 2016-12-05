import json
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from household.models import Household
from household.models import UserHousehold


def get_all_households(request):
    '''
    Return a list of all active households, each record containing
    - household unique id
    - household name
    '''
    info = []
    active_household_list = Household.objects.filter(active=True)
    for household in active_household_list:
        rec = {}
        rec['id'] = household.id
        rec['display'] = household.name
        info.append(rec)

    return JsonResponse(info, safe=False)


def save_household_user(request):
    '''
    Actualize the household user table
    '''
    r = {'result': True}
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))

        user = User.objects.get(username=request.user)
        user_household = UserHousehold.objects.get(user=user)
        household = Household.objects.get(id=data['id'])
        user_household.household = household
        user_household.save()

    return JsonResponse(r, safe=False)
