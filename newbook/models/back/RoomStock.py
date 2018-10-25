import uuid
from django.db import models
from django.utils import timezone
from newbook.models import Hotel, Room
from django.core.validators import MaxValueValidator, MinValueValidator


class RoomStock(models.Model):

    class Meta:
        db_table = 'roomStock'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    hotel_id = models.ForeignKey(
        'Hotel', to_field='hotel_id', on_delete=models.CASCADE)
    room_id = models.ManyToManyField('Room')
    date = models.DateField(blank=False, null=False)
    qty = models.IntegerField(default=0, validators=[MaxValueValidator(1000)])
    reserved_out = models.IntegerField(
        default=0, validators=[MaxValueValidator(1000)])

    def __int__(self):
        return self.qty
