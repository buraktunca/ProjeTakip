from main.models import Person
from django import forms

class EntranceForm(forms.Form):
    email = forms.EmailField(label='Email Adresiniz', max_length=100)
    password = forms.CharField(label='Şifreniz', max_length=100)
