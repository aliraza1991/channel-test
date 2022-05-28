

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from home.consumers import TestConsumer, TestConsumer2
# from django.conf.urls import url



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

ws_patterns = [
    path("ws/test/", TestConsumer),
    path("ws/new_consumer/", TestConsumer2),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
