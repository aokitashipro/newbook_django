from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from newbook.models import Hotel, Plan, Room, RoomStock
from django.views.generic import TemplateView
from django.views import View


class TestView(View):
  
  def get(self, request, *args, **kwargs):

    rooms = Room.objects.filter(hotel_id='N000001')

    hotels = Hotel.objects.select_related().all()

    context = {
      'rooms':rooms,
      'hotels':hotels,
    }
  
    return render(request, 'reserve/testpage.html', context)

testpage = TestView.as_view()
