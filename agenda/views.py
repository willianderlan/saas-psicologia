from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Sessao
from .forms import SessaoForm


@login_required
def lista_sessoes(request):

    sessoes = Sessao.objects.all().order_by('data', 'hora')

    return render(
        request,
        'agenda/lista.html',
        {'sessoes': sessoes}
    )


@login_required
def criar_sessao(request):

    if request.method == 'POST':

        form = SessaoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista_sessoes')

    else:

        form = SessaoForm()

    return render(
        request,
        'agenda/criar.html',
        {'form': form}
    )