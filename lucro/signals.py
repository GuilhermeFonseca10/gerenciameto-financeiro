from django.db.models.signals import post_delete
from django.dispatch import receiver
from lucro.models import Lucro

@receiver(post_delete, sender=Lucro)
def restore_saldo_on_delete(sender, instance, **kwargs):
    """Reverte o saldo da conta quando um lançamento é excluído"""
    if instance.conta:
        instance.conta.saldo -= instance.valor
        instance.conta.save()
