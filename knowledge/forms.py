from django import forms
from .models import Contacts, Contacts02, Contacts03, Contacts04, Contacts05, Contacts06q
from .models2 import Contacts06a

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('title', 'content')

class Contacts02Form(forms.ModelForm):
    class Meta:
        model = Contacts02
        fields = ('title', 'content')

class Contacts03Form(forms.ModelForm):
    class Meta:
        model = Contacts03
        fields = ('title', 'content')

class Contacts04Form(forms.ModelForm):
    class Meta:
        model = Contacts04
        fields = ('title', 'content')

class Contacts05Form(forms.ModelForm):
    class Meta:
        model = Contacts05
        fields = ('title', 'content')

class Contacts06qForm(forms.ModelForm):
    class Meta:
        model = Contacts06q
        fields = ('writer', 'password', 'title', 'content')

class Contacts06aForm(forms.ModelForm):
    class Meta:
        model = Contacts06a
        fields = ('reply', )