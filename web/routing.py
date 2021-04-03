from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('chart/', WSConsumer.as_asgi())
]