from django.urls import path

from .views import get_phone_data, find_phone

urlpatterns = [
    path('find_phone/', get_phone_data),
    path('', find_phone)
]
