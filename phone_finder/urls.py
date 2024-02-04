from django.urls import path

from phone_finder.views import get_phone_data, find_phone
# from phone_finder.tasks import update_csv_tables


# update_csv_tables()
urlpatterns = [
    path('find_phone/', get_phone_data),
    path('', find_phone)
]
