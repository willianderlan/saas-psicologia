from django.db import models

from agenda.models import Sessao


class Lembrete(models.Model):

    STATUS_CHOICES = [

        ('pendente', 'Pendente'),

        ('enviado', 'Enviado'),
    ]

    sessao = models.ForeignKey(
        Sessao,
        on_delete=models.CASCADE
    )

    mensagem = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f'Lembrete - {self.sessao.paciente.nome}'