from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from newbook.models import Hotel, Plan, Room, RoomStock
from django.views.generic import TemplateView
from django.views import View
from newbook.forms import CreatePlan


class TestView(View):
  
  def get(self, request, *args, **kwargs):

    rooms = Room.objects.filter(hotel_id='N000001')

    hotels = Hotel.objects.select_related().all()

    context = {
      'rooms':rooms,
      'hotels':hotels,
    }
  
    return render(request, 'hotel/testpage.html', context)

testpage = TestView.as_view()


class TestDesignView(View):
  
  def get(self, request, *args, **kwargs):

    rooms = Room.objects.filter(hotel_id='N000001')

    hotels = Hotel.objects.select_related().all()

    context = {
      'rooms':rooms,
      'hotels':hotels,
    }
  
    return render(request, 'hotel/hotel_base.html', context)

testdesign = TestDesignView.as_view()


class TestDesignView(View):

  def get(self, request, *args, **kwargs):

    rooms = Room.objects.filter(hotel_id='N000001')

    hotels = Hotel.objects.select_related().all()

    context = {
        'rooms': rooms,
        'hotels': hotels,
    }

    return render(request, 'hotel/hotel_base.html', context)


testdesign = TestDesignView.as_view()



class CreatePlanView(View):
    def get(self, request, *args, **kwargs):
        form = HotelForm(None, instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'hotel/CreatePlan.html', context)

    def post(self, request, *args, **kwargs):
        logger.info("You're in post!!!")

        # フォームを使ってバリデーション
        form = HotelForm(request.POST, instance=request.user)
        if not form.is_valid():
            return render(request, 'hotel/CreatePlan.html', {'form': form})

        # 変更を保存
        form.save()

        # フラッシュメッセージを画面に表示
        messages.info(request, "プロフィールを更新しました。")
        return redirect('/accounts/profile/')

createplan = CreatePlanView.as_view()
