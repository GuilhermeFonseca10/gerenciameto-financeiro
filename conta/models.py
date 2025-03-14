# coding: utf-8
from django.db import models
from django.urls import reverse

from usuario.models import Usuario


class Conta(models.Model):
    nome = models.CharField("Nome da conta", max_length=40)
    saldo = models.DecimalField("Saldo", max_digits=10, decimal_places=2, default=0)
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return str(self.nome)

    def __unicode__(self):
        return "%s: R$ %d" % (self.nome, self.saldo)

    class Meta:
        ordering = ["-saldo", "nome"]

    @property
    def get_absolute_url(self):
        return reverse("conta_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("conta_delete", args=[str(self.id)])



