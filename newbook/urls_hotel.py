from django.urls import path
from . import views_hotel

urlpatterns = [
    path('testpage', views_hotel.testpage, name='testpage'),
    path('testdesign', views_hotel.testdesign, name='testdesign'),
    path('createplan', views_hotel.createplan, name='createplan'),
]
