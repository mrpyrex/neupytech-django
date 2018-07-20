from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    phone = forms.CharField()
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : 'materialize-textarea'})) 
    