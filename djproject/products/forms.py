from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            "placeholder": "Your Title"
        })) # override the existing title field

    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['title', 'price', 'featured']
    
    # def clean_<field_name>():
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "lak" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            "placeholder": "Your Title"
        }))
    desc = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': "new-class-desc",
            'id': 'my-id-for-textarea',
            'rows': 20,
            'cols': 100
        }
    ))
    price = forms.DecimalField(initial=199.99)