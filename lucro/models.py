from django.db import models
from django.urls import reverse

from categoria.models import Categoria
from conta.models import Conta
from usuario.models import Usuario


# Create your models here.
class Lucro(models.Model):
    ganhos = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateField()

    categorias = models.ManyToManyField(Categoria)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.ganhos)

    def __unicode__(self):

        return "%s: R$ %d" % (self.ganhos, self.valor)

    class Meta:
        ordering = ["-valor", "ganhos"]

    @property
    def get_absolute_url(self):
        return reverse("lucro_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("lucro_delete", args=[str(self.id)])


# Create your models here.
