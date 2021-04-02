from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from webapp import consumers

websocket_urlPattern=[
    path('ws/polData/',consumers.DashConsumer),
]

application=ProtocolTypeRouter({
    #'http':
    'websockets':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})

