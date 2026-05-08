from django.db.models.signals import post_save

from django.dispatch import receiver

from .models import Sessao

from notificacoes.models import Lembrete


@receiver(post_save, sender=Sessao)
def criar_lembrete(sender, instance, created, **kwargs):

    if created:

        mensagem = (

            f'Olá {instance.paciente.nome}, '
            f'lembrando sua sessão em '
            f'{instance.data} às {instance.hora}.'
        )

        Lembrete.objects.create(

            sessao=instance,

            mensagem=mensagem
        )