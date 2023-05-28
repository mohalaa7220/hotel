from django.contrib import admin
from .models import (Amenity, Booking, Room, BookingUser)
# Register your models here.
admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(Booking)
admin.site.register(BookingUser)
