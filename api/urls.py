from django.urls import path
from api.store.views import *


urlpatterns = [
    path("location-list/", LocationView.as_view(), name="location-list"),
    path("truck/", TruckView.as_view(), name="truck"),
]