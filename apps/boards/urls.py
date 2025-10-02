from django.urls import path
from .views import BoardCreateView, BoardDetailView, BoardListView, BoardUpdateView, BoardDestroyView


urlpatterns = [
    path('', BoardListView.as_view()),
    path('create/', BoardCreateView.as_view()),
    path('board/<int:pk>/', BoardDetailView.as_view()),
    path('update/<int:pk>/', BoardUpdateView.as_view()),
    path('delete/<int:pk>/', BoardDestroyView.as_view()),
]