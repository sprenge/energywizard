import os
import platform
import sys
print ("version")
print(platform.python_version())
sys.path = ['/home/administrator/git'] + sys.path
sys.path = ['/home/administrator/git/energywizard'] + sys.path
sys.path = ['/usr/local/lib/python3.5/dist-packages'] + sys.path
print (sys.path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'energywizard.settings'
# import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
# application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()
