from django.urls import path
from . import views_reserve

urlpatterns = [
    path('testpage', views_reserve.testpage, name='testpage'),
]
