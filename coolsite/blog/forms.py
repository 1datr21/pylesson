from django import forms
from .models import *

class LeetForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'required': True}), )
