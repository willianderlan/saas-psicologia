from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Sessao
from .forms import SessaoForm


@login_required
def lista_sessoes(request):

    sessoes = Sessao.objects.do_usuario(
        request.user
    )

    return render(
        request,
        'agenda/lista.html',
        {'sessoes': sessoes}
    )


@login_required
def criar_sessao(request):

    if request.method == 'POST':

        form = SessaoForm(request.POST)

        form.fields['paciente'].queryset = (
            form.fields['paciente']
            .queryset
            .filter(usuario=request.user)
        )

        if form.is_valid():

            sessao = form.save(commit=False)

            if sessao.paciente.usuario != request.user:
                return redirect('lista_sessoes')

            sessao.save()

            return redirect('lista_sessoes')

    else:

        form = SessaoForm()

        form.fields['paciente'].queryset = (
            form.fields['paciente']
            .queryset
            .filter(usuario=request.user)
        )

    return render(
        request,
        'agenda/criar.html',
        {'form': form}
    )