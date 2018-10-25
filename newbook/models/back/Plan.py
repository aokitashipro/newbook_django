import uuid
from django.db import models
from django.utils import timezone
from newbook.models import Hotel, Room


class Plan(models.Model):

    class Meta:
        db_table = 'plan'
        unique_together = (('hotel_id', 'plan_id'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    hotel_id = models.ForeignKey('Hotel', to_field='hotel_id', on_delete=models.CASCADE)
    plan_id = models.CharField(max_length=10)
    plan_name = models.CharField(max_length=10)

    def __str__(self):
        return self.plan_name

class PlanRoomRelation(models.Model):

    class Meta:
        db_table = 'planRoomRelation'

    hotel_id = models.ForeignKey('Hotel', to_field='hotel_id', on_delete=models.CASCADE)
    plan_id = models.ForeignKey('Plan', to_field='plan_id', on_delete=models.CASCADE)
    room_id = models.ForeignKey('Room', to_field='room_id', on_delete=models.CASCADE)