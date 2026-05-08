from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Pagamento
from .forms import PagamentoForm


@login_required
def lista_pagamentos(request):

    pagamentos = Pagamento.objects.all().order_by('-criado_em')

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

        if form.is_valid():

            form.save()

            return redirect('lista_pagamentos')

    else:

        form = PagamentoForm()

    return render(
        request,
        'financeiro/criar.html',
        {'form': form}
    )