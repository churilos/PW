"""
ASGI config for TestApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from pyngrok import ngrok
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestApp.settings')

application = get_asgi_application()

tunnel = ngrok.connect(8080, authtoken_from_env=True)
print (f"Ingress established at {tunnel.url()}")
