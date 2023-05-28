from rest_framework import serializers
from .models import (Room, Amenity, Booking)


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'


class AddRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class RoomSerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'


# ------------ Booking -----------
class CreateBooking(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ('user', )

    def validate(self, attrs):
        check_in = attrs.get('check_in')
        check_out = attrs.get('check_out')
        if check_out and check_in and check_out <= check_in:
            raise serializers.ValidationError(
                'Check-out date must be after check-in date.')
        return attrs


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
