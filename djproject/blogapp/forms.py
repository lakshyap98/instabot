from django import forms
from .models import UserDetails

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'
    
    def clean(self):
        data = self.cleaned_data()