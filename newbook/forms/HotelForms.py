from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ObjectDoesNotExist
from newbook.models import Hotel, Plan, Room, RoomStock


class CreatePlan(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('plan_id', 'plan_name')

    def __init__(self, *args, **kwargs):
        super(CreatePlan, self).__init__(*args, **kwargs)
        self.fields['plan_id'].widget.attrs = {'placeholder': 'plan_id'}
        self.fields['plan_id'].required = True
        self.fields['plan_name'].widget.attrs = {'placeholder': 'plan_name'}
        self.fields['plan_name'].required = True

    def clean_plan_id(self):
        value = self.cleaned_data['plan_id']
        return value

    def clean_plan_name(self):
        value = self.cleaned_data['plan_name']
        return value