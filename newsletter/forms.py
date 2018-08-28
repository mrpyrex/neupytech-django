from django import forms
from .models import Join

class JoinForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Join
        fields = ['email']