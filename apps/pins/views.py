from rest_framework import generics
from .models import Pin
from .serializers import PinSerializer, PinCreateSerializer
from rest_framework import permissions


class PinListView(generics.ListAPIView):
    """
    Returns all pins
    """
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]

class PinCreateView(generics.CreateAPIView):
    """
    Creates a new pin
    """
    queryset = Pin.objects.all()
    serializer_class = PinCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class PinDeleteView(generics.DestroyAPIView):
    """
    Deletes a pin
    """
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]


class PinUpdateView(generics.UpdateAPIView):
    """
    Updates a pin
    """
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]

class PinDetailView(generics.RetrieveAPIView):
    """
    Returns a single pin by ID
    """
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]