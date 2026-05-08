from django import forms

from .models import Pagamento


class PagamentoForm(forms.ModelForm):

    class Meta:

        model = Pagamento

        fields = [
            'sessao',
            'valor',
            'status',
        ]

        widgets = {

            'sessao': forms.Select(attrs={
                'class': 'form-control'
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }