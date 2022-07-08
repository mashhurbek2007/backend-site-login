from dataclasses import fields
from .models import * 
from django import forms

class Sign(forms.ModelForm):
    class Meta():
        fields=(
            'username',
            'password',
        ) 

