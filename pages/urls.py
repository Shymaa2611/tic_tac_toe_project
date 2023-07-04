from django.urls import path
from . import views
from .views import index,game
urlpatterns=[
    path('', index),
    path('play/<room_code>', game),
]
