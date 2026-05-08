from django.urls import path

from .views import (
    lista_sessoes,
    criar_sessao
)

urlpatterns = [

    path(
        '',
        lista_sessoes,
        name='lista_sessoes'
    ),

    path(
        'nova/',
        criar_sessao,
        name='criar_sessao'
    ),
]