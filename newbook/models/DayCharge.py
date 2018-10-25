import uuid
from django.db import models
from django.utils import timezone
from newbook.models import Hotel
from django.core.validators import MaxValueValidator, MinValueValidator


class DayCharge(models.Model):

    class Meta:
        db_table = 'dayCharge'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    plan_id = models.CharField(max_length=10)
    date = models.DateField(blank=True, null=True)
    rank = models.CharField(max_length=3)
    person_num = models.IntegerField(default=0, validators=[MaxValueValidator(6)])
    charge = models.IntegerField(default=0)

    def __int__(self):
        return self.person_num
