from django.db import models

class mHotel(models.Model):
  class Meta:
    db_table = 'mHotel'

  hotel_id = models.CharField(max_length=7,primary_key=True,unique=True)
  chain_id = models.CharField(max_length=3,null=True)
  hotel_name = models.CharField(max_length=100)
  hotel_name_en = models.CharField(max_length=100)


  def __str__(self):
    return self.hotel_id
