
from django.urls import path
from .views import (RoomView, RoomDetails, AmenityView,
                    AmenityDetails, BookingView)

urlpatterns = [
    path('', RoomView.as_view(), name='add_room'),
    path('<int:pk>', RoomDetails.as_view(), name='details_room'),

    # ----- Amenity ------
    path('amenity/', AmenityView.as_view(), name='amenity'),
    path('amenity/<int:pk>', AmenityDetails.as_view(), name='amenity_details'),

    # ----- Booking ------
    path('booking/', BookingView.as_view(), name='booking'),
]
