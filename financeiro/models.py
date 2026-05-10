from django.db import models

from agenda.models import Sessao


class PagamentoManager(models.Manager):

    def do_usuario(self, user):

        return self.filter(
            sessao__paciente__usuario=user
        )


class Pagamento(models.Model):

    STATUS_CHOICES = [

        ('pendente', 'Pendente'),

        ('pago', 'Pago'),
    ]

    sessao = models.OneToOneField(
        Sessao,
        on_delete=models.CASCADE
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    objects = PagamentoManager()

    def __str__(self):

        return f'{self.sessao.paciente.nome} - {self.valor}'