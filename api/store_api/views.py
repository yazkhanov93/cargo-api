from geopy.distance import geodesic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema

from store.models import *
from .serializers import *


class CargoViews(APIView):
    @swagger_auto_schema(responses={"200":CargoDetailSerializer(many=True)})
    def get(self, request):
        cargo = Cargo.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result = paginator.paginate_queryset(cargo, request)
        serializer = CargoDetailSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(request_body=CargoAddSerializer(many=False))
    def post(self, request):
        location = Location.objects.all().only("id", "zip_code", "lat", "lng")
        pick_up = location.filter(zip_code=request.data["zip_code_from"])
        delivery = location.filter(zip_code=request.data["zip_code_to"])
        data = {"location_pick_up":pick_up[0].id, "location_delivery":delivery[0].id, "weight":request.data["weight"], "description":request.data["description"]}
        serializer = CargoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class CargoDetailView(APIView):
    @swagger_auto_schema(responses={"200":CargoDetailSerializer(many=False)})
    def get(self, request, pk):
        cargo = Cargo.objects.get(id=pk)
        truck = Truck.objects.all()
        truck_dist = []
        try:
            for i in truck:
                cargo_coordinate = (cargo.location_pick_up.lat, cargo.location_delivery.lng)
                truck_coordinate = (i.current_lat, i.current_lng)
                distance = (geodesic(cargo_coordinate, truck_coordinate).miles)
                truck_dist.append({"truck":i.number, "distance":distance, "value":"miles"})
            truck_dist = sorted(truck_dist, key=lambda k :k["distance"])
        except:
            pass
        serializer = CargoDetailSerializer(cargo, many=False)
        return Response({"Cargo":serializer.data, "trucks":truck_dist})


class EditCargo(APIView):
    @swagger_auto_schema(request_body=CargoDetailSerializer(many=False))
    def put(self, request, pk, format=None):
        cargo = Cargo.objects.get(id=pk)
        serializer = CargoDetailSerializer(cargo, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



class TruckView(APIView):
    @swagger_auto_schema(responses={"200":TruckSerializer(many=True)})
    def get(self, request):
        truck = Truck.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result = paginator.paginate_queryset(truck, request)
        serializer = TruckSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(request_body=TruckSerializer)
    def post(self, request):
        truck = request.data
        serializer = TruckSerializer(data=truck)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class TruckDetailView(APIView):
    @swagger_auto_schema(responses={"200":TruckSerializer(many=False)})
    def get(self, request, pk):
        truck = Truck.objects.get(number=pk)
        serializer = TruckSerializer(truck, many=False)
        return Response(serializer.data)
    

class LocationView(APIView):
    @swagger_auto_schema(responses={"200":LocationSerializer(many=True)})
    def get(self, request):
        location = Location.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result = paginator.paginate_queryset(location, request)
        serializer = LocationSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(request_body=LocationSerializer)
    def post(self, request):
        for data in request.data:
            serializer = LocationDetailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        return Response(status=status.HTTP_200_OK)


class LocationDetailView(APIView):
    @swagger_auto_schema(responses={"200":LocationSerializer(many=False)})
    def get(self, request, pk):
        location = Location.objects.get(id=pk)
        serializer = LocationSerializer(location, many=False)
        return Response(serializer.data)
