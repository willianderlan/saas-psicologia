from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pacientes.models import Paciente
from agenda.models import Sessao
from financeiro.models import Pagamento

from django.utils import timezone


@login_required
def home(request):

    total_pacientes = Paciente.objects.do_usuario(
        request.user
    ).count()

    total_sessoes = Sessao.objects.do_usuario(
        request.user
    ).count()

    total_pagamentos = Pagamento.objects.do_usuario(
        request.user
    ).count()

    pagamentos = Pagamento.objects.do_usuario(
        request.user
    )

    total_faturado = sum(
        pagamento.valor
        for pagamento in pagamentos
    )

    proximas_sessoes = Sessao.objects.do_usuario(
        request.user
    ).order_by('data', 'hora')[:5]

    context = {

        'total_pacientes': total_pacientes,
        'total_sessoes': total_sessoes,
        'total_pagamentos': total_pagamentos,
        'total_faturado': total_faturado,
        'proximas_sessoes': proximas_sessoes,

    }

    return render(
        request,
        'dashboard/home.html',
        context
    )