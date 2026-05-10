from django.db import models
from pacientes.models import Paciente


class SessaoManager(models.Manager):

    def do_usuario(self, user):

        return self.filter(
            paciente__usuario=user
        )


class Sessao(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE
    )

    data = models.DateField()

    hora = models.TimeField()

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    objects = SessaoManager()

    def __str__(self):

        return f'{self.paciente.nome} - {self.data}'