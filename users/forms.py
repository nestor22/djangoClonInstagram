"""user forms."""
# Django 
from django import forms

class Profileform(forms.Form):
    website = forms.URLField(max_length=200, required = True)
    biograpy = forms.CharField(max_length= 500, required = False)
    phone_number = forms.CharField(max_length= 20, required = False)
    picture = forms.ImageField()
    



