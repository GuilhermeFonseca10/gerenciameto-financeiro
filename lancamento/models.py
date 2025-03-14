from django.db import models
from django.urls import reverse

from categoria.models import Categoria
from conta.models import Conta
from usuario.models import Usuario


# Create your models here.
class Lancamento(models.Model):
    dispesa = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateField()

    categorias = models.ManyToManyField(
        Categoria,
        verbose_name='Categorias',
        blank=True
        )

    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, blank=True
    )
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.dispesa)

    def __unicode__(self):

        return "%s: R$ %d" % (self.dispesa, self.valor)

    class Meta:
        ordering = ["-valor", "dispesa"]

    @property
    def get_absolute_url(self):
        return reverse("lancamento_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("lancamento_delete", args=[str(self.id)])
    
