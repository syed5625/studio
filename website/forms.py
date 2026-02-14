from django import forms
from .models import Inquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["name", "email", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your Name"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Your Email"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Project details",
                "rows": 5
            }),
        }
