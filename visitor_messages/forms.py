from django import forms
from .models import VisitorMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = VisitorMessage
        field = ['name', 'email', 'message']
