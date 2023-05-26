from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Room(models.Model):
    ROOM_TYPES = [
        ('js', 'Junior Suite'),
        ('fr', 'Family Room'),
        ('dr', 'Double Room'),
        ('dx', 'Duplex Room'),
        ('dl', 'Deluxe Room'),
        ('sr', 'Superior Room'),
    ]
    type = models.CharField(max_length=120, choices=ROOM_TYPES)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    square = models.DecimalField(max_digits=6, decimal_places=2)
    amenities = models.ManyToManyField(
        'Amenity', related_name='room_amenities')

    def save(self, *args, **kwargs):
        self.type = self.type.lower()
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.square} sqm - ${self.price}"


class Amenity(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Booking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    num_adults = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    num_children = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    num_rooms = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_booking')
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='room_booking')

    def __str__(self):
        return f"Booking {self.id}: {self.check_in} to {self.check_out} ({self.num_rooms} room{'s' if self.num_rooms > 1 else ''}, {self.num_adults} adult{'s' if self.num_adults > 1 else ''}, {self.num_children} child{'ren' if self.num_children > 1 else ''})"

    class Meta:
        verbose_name_plural = "bookings"
