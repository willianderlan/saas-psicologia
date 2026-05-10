from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Pagamento
from .forms import PagamentoForm


@login_required
def lista_pagamentos(request):

    pagamentos = Pagamento.objects.do_usuario(
        request.user
    )

    total_faturado = 0

    for pagamento in pagamentos:

        if pagamento.status == 'pago':

            total_faturado += pagamento.valor

    context = {

        'pagamentos': pagamentos,

        'total_faturado': total_faturado,
    }

    return render(
        request,
        'financeiro/lista.html',
        context
    )


@login_required
def criar_pagamento(request):

    if request.method == 'POST':

        form = PagamentoForm(request.POST)

        form.fields['sessao'].queryset = (
            form.fields['sessao']
            .queryset
            .filter(
                paciente__usuario=request.user
            )
        )

        if form.is_valid():

            pagamento = form.save(commit=False)

            if pagamento.sessao.paciente.usuario != request.user:
                return redirect('lista_pagamentos')

            pagamento.save()

            return redirect('lista_pagamentos')

    else:

        form = PagamentoForm()

        form.fields['sessao'].queryset = (
            form.fields['sessao']
            .queryset
            .filter(
                paciente__usuario=request.user
            )
        )

    return render(
        request,
        'financeiro/criar.html',
        {'form': form}
    )