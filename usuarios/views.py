from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pacientes.models import Paciente
from agenda.models import Sessao

from datetime import date


@login_required
def home(request):

    total_pacientes = Paciente.objects.count()

    hoje = date.today()

    sessoes_hoje = Sessao.objects.filter(
        data=hoje
    ).count()

    proximas_sessoes = Sessao.objects.filter(
        data__gte=hoje
    ).order_by('data', 'hora')[:5]

    context = {

        'total_pacientes': total_pacientes,

        'sessoes_hoje': sessoes_hoje,

        'proximas_sessoes': proximas_sessoes,
    }

    return render(
        request,
        'home.html',
        context
    )