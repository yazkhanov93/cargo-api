from __future__ import absolute_import, unicode_literals
import random

from celery import shared_task


from .models import *



@shared_task
def change_coordinates():
    message = "truck coordinates was changed"
    coordinates = Location.objects.all().only("lat", "lng")
    trucks = Truck.objects.all()
    for i in trucks:
        l = random.choice(coordinates)
        i.current_lat = l.lat
        i.current_lng = l.lng
        i.save()
    return message