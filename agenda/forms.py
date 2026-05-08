from django import forms
from .models import Sessao


class SessaoForm(forms.ModelForm):

    class Meta:

        model = Sessao

        fields = [
            'paciente',
            'data',
            'hora',
            'observacoes',
        ]

        widgets = {

            'paciente': forms.Select(attrs={
                'class': 'form-control'
            }),

            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'hora': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'observacoes': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }