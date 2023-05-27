from rest_framework import generics, status
from .serializers import (
    RoomSerializer, AddRoomSerializer, AmenitySerializer, CreateBooking)
from .models import (Room, Amenity, Booking)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


#  ------------ (Add , Get Rooms) --------------
class RoomView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.prefetch_related('amenities')

    def post(self, request):
        serializer_class = AddRoomSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response({"message": "Room created successfully"}, status=status.HTTP_200_OK)


#  ------------ (Details Room , update , delete) ------------
class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.prefetch_related('amenities')

    def update(self, request, pk=None):
        serializer_class = AddRoomSerializer(
            instance=self.get_object(), data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response({"message": "Room Updated successfully"}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Room Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


#  ------------ (Add , Get Amenity) ------------
class AmenityView(generics.ListCreateAPIView):
    serializer_class = AmenitySerializer
    queryset = Amenity.objects.all()


#  ------------ (Details Amenity , update , delete) ------------
class AmenityDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AmenitySerializer
    queryset = Amenity.objects.all()


class BookingView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateBooking
    queryset = Booking.objects.select_related('user', 'room').all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
