from django.db import models
from django.utils import timezone
from newbook.models import Hotel, Plan

class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_id = models.CharField(max_length=10)
    room_name = models.CharField(max_length=10)
    plan_id = models.ManyToManyField(Plan)

    def __str__(self):
        return self.room_id
