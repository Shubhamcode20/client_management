from django import forms
from .models import ClientProfile
from django.contrib.auth.models import User

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ['name', 'primary_number', 'country_code']