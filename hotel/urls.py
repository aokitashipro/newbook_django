from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('testpage/', views.testpage.testpage_function, name='testpage'),
]

