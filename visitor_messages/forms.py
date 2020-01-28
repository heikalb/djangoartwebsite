from django import forms
from .models import VisitorMessage
import random


class ContactForm(forms.ModelForm):
    int_1 = random.randint(1, 10)
    int_2 = random.randint(1, 10)
    validation_label = f'Validation: ({int_1} + {int_2} = )'
    validation = forms.IntegerField(label=validation_label, required=True,)

    class Meta:
        model = VisitorMessage
        fields = ['name', 'email', 'message']

    def clean_validation(self):
        answer = int(self.cleaned_data.get('validation'))

        if not answer == self.int_1 + self.int_2:
            raise forms.ValidationError('Incorrect sum')

        return answer

