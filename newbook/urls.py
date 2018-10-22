from django.urls import path
from . import views_reserve
from newbook.models import Hotel

app_name = 'newbook'

urlpatterns = [
    path('<str:pk>/reserve/', views_reserve.testpage, name='testpage'),
]
