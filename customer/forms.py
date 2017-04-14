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

    start_date = forms.DateField(widget=forms.DateInput(format = '%Y%m%d'),
                                 input_formats=('%Y%m%d',))
    end_date = forms.DateField(widget=forms.DateInput(format = '%Y%m%d'),
                               input_formats=('%Y%m%d',),
                               required=False)

    class Meta:
        model = Customer03
        fields = ('title', 'content', 'start_date', 'end_date')

class Customer04Form(forms.ModelForm):
    class Meta:
        model = Customer04
        fields = ('title', )

class Customer04rForm(forms.ModelForm):
    class Meta:
        model = Customer04
        fields = ('content', )
