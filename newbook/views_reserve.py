from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from newbook.models import Hotel, Plan, Room, RoomStock
from django.views.generic import TemplateView
from django.views import View


class TestView(View):
  
  def get(self, request, *args, **kwargs):

    hotels = Hotel.objects.order_by('hotel_id')
    plans = Plan.objects.order_by('plan_id')
    planHotels = Plan.objects.select_related('hotel_id')

    context = {
      'hotels':hotels,
      'plans':plans, 
      'planHotels':planHotels,
    }

    return render(request, 'reserve/testpage.html', context)

testpage = TestView.as_view()
