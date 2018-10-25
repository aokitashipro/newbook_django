import uuid
from django.db import models
from django.utils import timezone
from newbook.models import Hotel, Room
from django.core.validators import MaxValueValidator, MinValueValidator


class RoomStock(models.Model):

    class Meta:
        db_table = 'roomStock'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    room_id = models.CharField(max_length=10)
    date = models.DateField(blank=True, null=True)
    qty = models.IntegerField(default=0, validators=[MaxValueValidator(1000)])
    reserved_out = models.IntegerField(default=0, validators=[MaxValueValidator(1000)])

    def __int__(self):
        return self.qty
