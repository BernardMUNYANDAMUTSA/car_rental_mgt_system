from django.urls import path
from .consumers import BookingConsumer, UserInputConsumer
from .consumers import RealTimeUpdateConsumer
from . import consumers

websocket_urlpatterns = [
    path('ws/updates/', BookingConsumer.as_asgi()),
    #path('ws/user-input/', UserInputConsumer.as_asgi()),
    path('ws/user-input/', consumers.UserInputConsumer.as_asgi()),
    #path('ws/user-input/', RealTimeUpdateConsumer.as_asgi()),
]