# chat/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path('ws/chat/(?P<village_id>\w+)/(?P<user_id>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
    # re_path(r'ws/chat/(?P<village_id>[0-9a-fA-F-]+)/(?P<user_id>[0-9a-fA-F-]+)/$', consumers.ChatRoomConsumer.as_asgi()),

]
