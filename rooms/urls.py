
from django.urls import path
from .views import (RoomView, RoomDetails)

urlpatterns = [
    path('', RoomView.as_view(), name='add_room'),
    path('<int:pk>', RoomDetails.as_view(), name='details_room'),
]
