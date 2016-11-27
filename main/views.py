from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from gezin.models import GebruikerGezin


def is_user_member_of(user, group):
    '''
    Check if user (by username) is member of a certain group
    '''
    if user.is_superuser:
        return True
    return user.groups.filter(name=group).exists()


@login_required
def homepage(request):
    info = {}
    user = User.objects.get(username=request.user)
    info['first_name'] = user.first_name
    info['last_name'] = user.last_name
    try:
        gezin_rec = GebruikerGezin.objects.get(user=user)
        gezin = gezin_rec.gezin
    except Exception as e:
        print (e)
        return render_to_response("fatal_error.html", info, RequestContext(request))

    info['gezin'] = str(gezin.naam)
    info['energiemeester'] = is_user_member_of(user, 'energiemeester')
    return render_to_response("homepage.html", info, RequestContext(request))


def auth_login(request):
    '''
    Login request from a user
    '''

    state = ""
    context = {'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect = request.POST['next']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                # return HttpResponseRedirect(request.POST.get('next', '/'))
                if redirect == "":
                    redirect = "/"
                return HttpResponseRedirect(redirect)
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    context['state'] = state

    return render_to_response("login.html", context, RequestContext(request))


def auth_logoff(request):
    '''
    Log off request from a user
    '''
    logout(request)
    return HttpResponseRedirect('/')
