from rest_framework import serializers
from store.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"


class CargoAddSerializer(serializers.Serializer):
    zip_code_from = serializers.CharField(max_length=100)
    zip_code_to = serializers.CharField(max_length=100)
    weight = serializers.FloatField()
    description = serializers.CharField()


class CargoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"


class CargoDetailSerializer(serializers.ModelSerializer):
    location_pick_up = LocationSerializer()
    location_delivery = LocationSerializer()
    class Meta:
        model = Cargo
        fields = "__all__"



class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"

