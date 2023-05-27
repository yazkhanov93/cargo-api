from django.contrib import admin
from .models import *


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["city", "state"]


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ["number", "load_capacity"]


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ["weight", "location_pick_up", "location_delivery"]