from django.db import models
from django.utils import timezone

class Hotel(models.Model):
  hotel_id = models.CharField(max_length=10, primary_key=True)
  hotel_name = models.CharField(max_length=255)
  hotel_name_en = models.CharField(max_length=255, null=True)

  def __str__(self):
    return self.hotel_id