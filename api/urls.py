from django.urls import path
from api.store_api.views import *


urlpatterns = [
    path("location-list/", LocationView.as_view(), name="location-list"),
    path("location/<int:pk>/", LocationDetailView.as_view(), name="location"),
    path("truck-list/", TruckView.as_view(), name="truck-list"),
    path("truck/<str:pk>/", TruckDetailView.as_view(), name="truck"),
    path("cargo-list/", CargoViews.as_view(), name="cargo-list"),
    path("cargo/<int:pk>/", CargoDetailView.as_view(), name="cargo"),
    path("ecit-cargo/<int:pk>/", EditCargo.as_view(), name="edit-cargo")
]