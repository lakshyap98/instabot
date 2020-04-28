from django import forms
from .models import *


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    # def clean_title(self):
    #     import pdb; pdb.set_trace()