from django.urls import path
from . import views_api

urlpatterns = [
    path('testpage', views_hotel.testpage, name='testpage'),
]
