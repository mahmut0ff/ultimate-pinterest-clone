from django.urls import path
from .views import PinListView, PinCreateView, PinUpdateView, PinDeleteView, PinDetailView

urlpatterns = [
    path('', PinListView.as_view()),
    path('pin/<int:pk>/', PinDetailView.as_view()),
    path('create/', PinCreateView.as_view()),
    path('update/<int:pk>/', PinUpdateView.as_view()),
    path('delete/<int:pk>/', PinDeleteView.as_view()),
]