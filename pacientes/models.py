from django.db import models

from django.contrib.auth.models import User
from django.db import models


class PacienteManager(models.Manager):

    def do_usuario(self, user):

        return self.filter(usuario=user)

class Paciente(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=255)

    objects = PacienteManager()

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome