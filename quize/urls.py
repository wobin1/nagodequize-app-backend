from django.urls import path
from .views import QuizeListCreateView, QuizeRetrieveUpdateDestroyView
from .views import QuizeRegisterView


urlpatterns = [
    path('quizes/register/', QuizeRegisterView.as_view(), name='quize-register'),
    path('quizes/', QuizeListCreateView.as_view(), name='quize-list-create'),
    path('quizes/<int:pk>/', QuizeRetrieveUpdateDestroyView.as_view(), name='quize-retrieve-update-destroy'),
]

