from django.urls import path
from .views import get_document

urlpatterns = [
    path("document/<int:pk>/", get_document),
]