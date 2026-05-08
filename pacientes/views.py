from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def lista_pacientes(request):

    pacientes = Paciente.objects.all()

    return render(
        request,
        'pacientes/lista.html',
        {'pacientes': pacientes}
    )


@login_required
def criar_paciente(request):

    if request.method == 'POST':

        form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('lista_pacientes')

    else:
        form = PacienteForm()

    return render(
        request,
        'pacientes/criar.html',
        {'form': form}
    )
@login_required
def editar_paciente(request, paciente_id):

    paciente = get_object_or_404(
        Paciente,
        id=paciente_id
    )

    if request.method == 'POST':

        form = PacienteForm(
            request.POST,
            instance=paciente
        )

        if form.is_valid():

            form.save()

            return redirect('lista_pacientes')

    else:

        form = PacienteForm(instance=paciente)

    return render(
        request,
        'pacientes/editar.html',
        {
            'form': form,
            'paciente': paciente
        }
    )


@login_required
def deletar_paciente(request, paciente_id):

    paciente = get_object_or_404(
        Paciente,
        id=paciente_id
    )

    if request.method == 'POST':

        paciente.delete()

        return redirect('lista_pacientes')

    return render(
        request,
        'pacientes/deletar.html',
        {
            'paciente': paciente
        }
    )