from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Register

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= Register
        fields="__all__"