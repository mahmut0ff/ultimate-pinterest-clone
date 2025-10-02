from rest_framework import generics
from .models import Pin
from .serializers import PinSerializer, PinCreateSerializer
from rest_framework import permissions


class PinListView(generics.ListAPIView):
    """
    API view to list all Pin instances.
    This view returns a list of all pins available in the system.
    Access is restricted to authenticated users.
    Attributes:
        queryset (QuerySet): All Pin objects.
        serializer_class (Serializer): Serializer for Pin objects.
        permission_classes (list): List of permission classes; only authenticated users can access.
    """

    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]


class PinCreateView(generics.CreateAPIView):
    """
    API view for creating a new Pin instance.
    This view allows authenticated users to create new pins. The created pin will be associated
    with the currently authenticated user as the owner.
    Attributes:
        queryset (QuerySet): The queryset of all Pin objects.
        serializer_class (Serializer): The serializer class used for validating and deserializing input.
        permission_classes (list): List of permission classes that determine access to this view.
    Methods:
        perform_create(serializer):
            Saves the new Pin instance with the current user set as the owner.
    """

    queryset = Pin.objects.all()
    serializer_class = PinCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class PinDeleteView(generics.DestroyAPIView):
    """
    API view for deleting a Pin instance.
    This view allows authenticated users to delete a Pin by its primary key (pk).
    Attributes:
        queryset (QuerySet): The queryset of all Pin objects.
        serializer_class (Serializer): The serializer class used for Pin objects.
        permission_classes (list): List of permission classes; only authenticated users are allowed.
    """

    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]


class PinUpdateView(generics.UpdateAPIView):
    """
    API view for updating an existing Pin instance.
    This view allows authenticated users to update the details of a Pin.
    It uses the PinSerializer for validating and saving the data.
    Only authenticated users are permitted to perform update operations.
    Attributes:
        queryset (QuerySet): The queryset of all Pin objects.
        serializer_class (Serializer): The serializer class used for Pin objects.
        permission_classes (list): List of permission classes; only authenticated users are allowed.
    """
    
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]


class PinDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving a specific Pin instance by its primary key (pk).
    This view allows authenticated users to retrieve the details of a Pin.
    Attributes:
        queryset (QuerySet): The queryset of all Pin objects.
        serializer_class (Serializer): The serializer class used for Pin objects.
        permission_classes (list): List of permission classes; only authenticated users are allowed.
    """

    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticated]