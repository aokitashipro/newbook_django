from django.db import models
from django.utils import timezone
from newbook.models import Hotel

class Plan(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    plan_id = models.CharField(max_length=10)
    plan_name = models.CharField(max_length=10)

    def __str__(self):
        return self.plan_id
