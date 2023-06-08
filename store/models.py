import random
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=100, unique=True)
    lat = models.FloatField(unique=True)
    lng = models.FloatField(unique=True)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.city


class Truck(models.Model):
    number = models.CharField(max_length=10, unique=True, primary_key=True)
    current_lat = models.FloatField()
    current_lng = models.FloatField()
    load_capacity = models.FloatField()

    class Meta:
        verbose_name_plural = "Trucks"

    def __str__(self):
        return self.number



class Cargo(models.Model):
    location_pick_up = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location_pick_up")
    location_delivery = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location_delivery")
    weight = models.FloatField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.location_pick_up.city