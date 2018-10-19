from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.utils.translation import gettext as _

"""
def login_function(request):
  return HttpResponse("login")

""" 
def login_function(request):
    view_trans = _('これはビューの翻訳です')
    context = {'view_trans': view_trans}
    return render(request, "mypage/login.html", context)

