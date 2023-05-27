import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from store.models import *
from .serializers import *


class TruckView(APIView):
    @swagger_auto_schema(responses={"200":TruckSerializer(many=True)})
    def get(self, request):
        truck = Truck.objects.all()
        serializer = TruckSerializer(truck, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TruckSerializer)
    def post(self, request):
        truck = request.data
        serializer = TruckSerializer(data=truck)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class LocationView(APIView):
    @swagger_auto_schema(responses={"200":LocationSerializer(many=True)})
    def get(self, request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LocationSerializer)
    def post(self, request):
        for data in request.data:
            serializer = LocationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        return Response(status=status.HTTP_200_OK)