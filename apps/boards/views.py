from rest_framework import generics, permissions
from .models import Board
from .serializers import BoardSerializer


class BoardListView(generics.ListAPIView):
    """
    API view to list all Board instances.

    This view returns a list of all boards available in the system.
    Access is restricted to authenticated users.

    Attributes:
        queryset (QuerySet): All Board objects.
        serializer_class (Serializer): Serializer for Board objects.
        permission_classes (list): List of permission classes; only authenticated users can access.
    """
    
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]


class BoardCreateView(generics.CreateAPIView):
    """
    API view for creating a new Board instance.
    This view allows authenticated users to create new boards. The created board will be associated
    with the currently authenticated user as the owner.
    Attributes:
        queryset (QuerySet): The queryset of all Board objects.
        serializer_class (Serializer): The serializer class used for validating and deserializing input.
        permission_classes (list): List of permission classes that determine access to this view.
    Methods:
        perform_create(serializer):
            Saves the new Board instance with the current user set as the owner.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardUpdateView(generics.UpdateAPIView):
    """
    API view for updating an existing Board instance.
    This view allows authenticated users to update the details of a Board.
    It uses the BoardSerializer for validating and saving the data.
    Only authenticated users are permitted to perform update operations.
    Attributes:
        queryset (QuerySet): The queryset of all Board objects.
        serializer_class (Serializer): The serializer class used for Board objects.
        permission_classes (list): List of permission classes; only authenticated users are allowed.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]


class BoardDestroyView(generics.DestroyAPIView):
    """
    API view for deleting a Board instance.
    This view allows authenticated users to delete a specific Board object.
    It uses the DestroyAPIView from Django REST Framework, which provides
    the default destroy behavior.
    Attributes:
        queryset (QuerySet): The queryset of all Board objects.
        serializer_class (Serializer): The serializer class for Board objects.
        permission_classes (list): List containing IsAuthenticated permission class,
            ensuring only authenticated users can perform the delete operation.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]


class BoardDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving a single Board instance by its ID.
    This view allows authenticated users to fetch the details of a specific Board object.
    It uses the RetrieveAPIView from Django REST Framework, which provides
    the default retrieve behavior.
    Attributes:
        queryset (QuerySet): The queryset of all Board objects.
        serializer_class (Serializer): The serializer class for Board objects.
        permission_classes (list): List containing IsAuthenticated permission class,
            ensuring only authenticated users can access the board details.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]