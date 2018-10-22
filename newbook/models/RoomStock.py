from django.db import models
from django.utils import timezone
from newbook.models import Hotel, Room
from django.core.validators import MaxValueValidator, MinValueValidator

class RoomStock(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    qty = models.IntegerField(default=0, validators=[MaxValueValidator(1000)])
    reserved_out = models.IntegerField(default=0, validators=[MaxValueValidator(1000)])

    def __int__(self):
        return self.qty
