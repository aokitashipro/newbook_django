from django.conf.urls import include, url
from django.urls import path
from newbook import views


urlpatterns = [
    path('hotel', newbook.views.hotel.index.index, name='hotel'),
    path('mainte', newbook.views.mainte.index.index, name='mainte'),
    path('member', newbook.views.member.index.index, name='member'),
    path('mypage', newbook.views.mypage.index.index, name='mypage'),
    path('reserve', newbook.views.reserve.index.index, name='reserve'),
]



