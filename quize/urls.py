from django.urls import path
from .views import QuizeListCreateView, QuizeRetrieveUpdateDestroyView
from .views import quize_create

urlpatterns = [
    path('quize_create', quize_create, name='quize-create'),
    path('quizes/', QuizeListCreateView.as_view(), name='quize-list-create'),
    path('quizes/<int:pk>/', QuizeRetrieveUpdateDestroyView.as_view(), name='quize-retrieve-update-destroy'),
]

