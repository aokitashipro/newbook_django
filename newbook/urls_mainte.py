from django.urls import path
from . import views_mainte


urlpatterns = [
    path('testpage', views_mainte.testpage, name='testpage'),
]
