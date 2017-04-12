from django import forms
from .models import Counsel01, Counsel02

class Counsel01Form(forms.ModelForm):

    class Meta:
        model = Counsel01
        fields = ('writer', 'title', 'fp', 'content', 'photo', 'password', )

class Counsel02Form(forms.ModelForm):

    class Meta:
        model = Counsel02
        fields = ('writer', 'fp', 'content', 'agree', 'birth', 'tel', 'email',
                  'address', 'job', 'area', 'time')