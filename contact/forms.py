from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    sender = forms.EmailField(required=True)
    phone = forms.IntegerField()
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : 'materialize-textarea'}))
    
    
