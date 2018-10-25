import uuid
from django.db import models
from django.utils import timezone
from newbook.models import Hotel, Plan

class Room(models.Model):

    class Meta:
        db_table = 'room'
        unique_together = (('hotel_id', 'room_id'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    room_id = models.CharField(max_length=10)
    room_name = models.CharField(max_length=10)

    def __str__(self):
        return self.room_name
