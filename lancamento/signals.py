from django.db.models.signals import post_delete
from django.dispatch import receiver
from lancamento.models import Lancamento

@receiver(post_delete, sender=Lancamento)
def restore_saldo_on_delete(sender, instance, **kwargs):
    """Reverte o saldo da conta quando um lançamento é excluído"""
    if instance.conta:
        instance.conta.saldo += instance.valor
        instance.conta.save()
