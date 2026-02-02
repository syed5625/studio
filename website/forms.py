from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["name", "email", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your Name",
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Your Email",
                "class": "form-control"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Tell us about your project",
                "rows": 5,
                "class": "form-control"
            }),
        }
