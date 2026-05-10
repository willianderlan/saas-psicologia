from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pacientes.models import Paciente
from agenda.models import Sessao
from financeiro.models import Pagamento


@login_required
def home(request):

    total_pacientes = Paciente.objects.filter(
        usuario=request.user
    ).count()

    total_sessoes = Sessao.objects.filter(
        paciente__usuario=request.user
    ).count()

    total_pagamentos = Pagamento.objects.filter(
        sessao__paciente__usuario=request.user
    ).count()

    pagamentos = Pagamento.objects.filter(
        sessao__paciente__usuario=request.user
    )

    total_faturado = sum(
        pagamento.valor
        for pagamento in pagamentos
    )

    context = {

        'total_pacientes': total_pacientes,
        'total_sessoes': total_sessoes,
        'total_pagamentos': total_pagamentos,
        'total_faturado': total_faturado,

    }

    return render(
        request,
        'dashboard/home.html',
        context
    )