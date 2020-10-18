from django import forms
from django.forms import ModelForm

from home.models import postform


class postform(forms.ModelForm):
    class Meta:
        
        model = postform
        fields = ['author','phone','message']

