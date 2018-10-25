import uuid
from django.db import models
from django.utils import timezone
from newbook.models import Hotel, Room


class Plan(models.Model):

    class Meta:
        db_table = 'plan'
        unique_together = (('hotel_id', 'plan_id'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    plan_id = models.CharField(max_length=10)
    plan_name = models.CharField(max_length=10)

    def __str__(self):
        return self.plan_id
