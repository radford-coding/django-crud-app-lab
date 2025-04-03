from django import forms
from .models import Picking

class PickingForm(forms.ModelForm):
    class Meta:
        model = Picking
        fields = ['date', 'haul']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'pick a date',
                    'type': 'date'
                }
            )
        }