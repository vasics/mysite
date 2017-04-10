from django import forms
from .models import Counsel01

class Counsel01Form(forms.ModelForm):
    class Meta:
        model = Counsel01
        fields = ('writer', 'title', 'fp', 'content', 'photo')