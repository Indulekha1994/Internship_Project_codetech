from django.urls import path
from .views import save_usage, weekly_report

urlpatterns = [
    path('save/', save_usage),
    path('weekly/', weekly_report),
]