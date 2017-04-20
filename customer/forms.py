from django import forms
from .models import Customer01, Customer02, Customer03, Customer04
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

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
        fields = ('start_date', 'end_date')

class Customer04Form(forms.ModelForm):
    class Meta:
        model = Customer04
        fields = ('title', )

class Customer04rForm(forms.ModelForm):
    class Meta:
        model = Customer04
        fields = ('content', )
