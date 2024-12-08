"""
ASGI config for car_rental_mgt_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import rental_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_rental_mgt_system.settings')

#application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            rental_app.routing.websocket_urlpatterns
        )
    ),
})
