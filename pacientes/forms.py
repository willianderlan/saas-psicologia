from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):

    class Meta:

        model = Paciente

        fields = [
            'nome',
            'telefone',
            'email',
            'observacoes',
        ]

        widgets = {

            'nome': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'telefone': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'observacoes': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }