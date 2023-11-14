"""
WSGI config for DjangoPro1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoPro1.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root="/DjangoPro1-123/petapp/static/")
application.add_files("/DjangoPro1-123/petapp/static/", prefix="more-files/")