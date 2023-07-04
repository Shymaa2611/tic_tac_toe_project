from django.conf.urls import url
from pages.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', TicTacToeConsumer.as_asgi()),
]