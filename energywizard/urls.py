"""energywizard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main.views import auth_login, auth_logoff
from graphs.views import get_meter_values
from graphs.views import graph_home


urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^household/', include('household.urls')),
    url(r'^meter/', include('meter.urls')),
    url(r'^login/', auth_login),
    url(r'^logout/', auth_logoff),
    url(r'^graph/get_meter_values/(?P<household>.*)/(?P<meter>.*)/$', get_meter_values),
    url(r'^graph/home/(?P<household>.*)/(?P<meter>.*)/$', graph_home),

]
