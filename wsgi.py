import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
application = WSGIHandler()
