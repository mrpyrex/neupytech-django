from django import forms
from .models import Join

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get("email")
            # qs = Join.objects.filter(email_iexact=email)
            # if qs.exists():
            #     raise forms.ValidationError("We have your email aready")
            return email
