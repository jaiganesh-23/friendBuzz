"""
WSGI config for friendbuzz_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import eventlet
import socketio
from .views import sio

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'friendbuzz_backend.settings')

django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)

eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8000)), application)