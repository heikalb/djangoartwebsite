from django import forms
from .models import VisitorMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = VisitorMessage
        fields = ['name', 'email', 'message']
