from django.urls import path
from . import views_mypage

urlpatterns = [
    path('testpage', views_reserve.testpage, name='testpage'),
]
