from rest_framework import generics, status
from .serializers import (RoomSerializer, AddRoomSerializer)
from .models import Room, Amenity
from rest_framework.response import Response


class RoomView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.prefetch_related('amenities')

    def post(self, request):
        serializer_class = AddRoomSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response({"message": "Room created successfully"}, status=status.HTTP_200_OK)


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
