from rest_framework import serializers
from store.models import *


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"