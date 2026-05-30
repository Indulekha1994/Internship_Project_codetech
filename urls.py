from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.indexView, name='home'),
    
    path('<str:room_name>/<str:username>/', views.roomView, name='room'),
]


