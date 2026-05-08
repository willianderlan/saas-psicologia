from django.urls import path

from .views import (
    lista_pacientes,
    criar_paciente,
    editar_paciente,
    deletar_paciente
)

urlpatterns = [

    path(
        '',
        lista_pacientes,
        name='lista_pacientes'
    ),

    path(
        'novo/',
        criar_paciente,
        name='criar_paciente'
    ),

    path(
        'editar/<int:paciente_id>/',
        editar_paciente,
        name='editar_paciente'
    ),

    path(
        'deletar/<int:paciente_id>/',
        deletar_paciente,
        name='deletar_paciente'
    ),
]