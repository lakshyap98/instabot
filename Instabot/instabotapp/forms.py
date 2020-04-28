from django import forms
from .models import *


class DetailForm(forms.ModelForm):
    class Meta:
        model = DetailAccount
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = '__all__'
