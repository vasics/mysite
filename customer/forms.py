from django import forms
from .models import Customer01, Customer02, Customer03, Customer04

class Customer01Form(forms.ModelForm):
    class Meta:
        model = Customer01
        fields = ('title', 'content')

class Customer02Form(forms.ModelForm):
    class Meta:
        model = Customer02
        fields = ('title', 'content')

class Customer03Form(forms.ModelForm):
    class Meta:
        model = Customer03
        fields = ('title', 'content')

class Customer04Form(forms.ModelForm):
    class Meta:
        model = Customer04
        fields = ('writer', 'title', 'content', 'password')
