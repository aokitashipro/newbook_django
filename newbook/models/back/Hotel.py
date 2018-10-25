import uuid
from django.db import models
from django.utils import timezone


class Hotel(models.Model):

    class Meta:
        db_table = 'hotel'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    hotel_id = models.CharField(max_length=10, unique=True)
    hotel_name_ja = models.CharField(max_length=255)
    hotel_name_en = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.hotel_name_ja
