#coding: utf-8
from django.db import models
from django.urls import reverse
from usuario.models import Usuario
from django.db.models.signals import post_save
from django.dispatch import receiver

class Conta(models.Model):
    descricao = models.CharField(u'Descrição', max_length=40)
    saldo = models.DecimalField(u'Saldo', max_digits=10, decimal_places=2, default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.descricao)

    def __unicode__(self):
        return '%s: R$ %d' % (self.descricao, self.saldo)

    class Meta:
        ordering = ['-saldo','descricao']
        


    @property
    def get_absolute_url(self):
        return reverse('conta_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('conta_delete', args=[str(self.id)])

from lancamento.models import Lancamento
@receiver(post_save, sender=Lancamento)
def update_saldo(sender, instance, **kwargs):
    instance.conta.saldo -= instance.valor
    instance.conta.save()

from lucro.models import Lucro
@receiver(post_save, sender=Lucro)
def update_saldo_lucro(sender, instance, **kwargs):
    instance.conta.saldo += instance.valor
    instance.conta.save()
