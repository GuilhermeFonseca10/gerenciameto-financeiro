from django.db import models
from categoria.models import Categoria
from django.core.urlresolvers import reverse
from usuario.models import Usuario
from conta.models import Conta
# Create your models here.
class Lancamento(models.Model):
    dispesa = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateField()
    
    categorias = models.ManyToManyField(Categoria)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True, blank=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, null=True, blank=True)
    
   

    def __str__(self):
        return str()

    def __unicode__(self):
        
        return '%s: R$ %d' % (self.dispesa, self.valor)

    class Meta:
        ordering = ['-valor','dispesa']


    @property
    def get_absolute_url(self):
        return reverse('lancamento_update', args=[str(self.id)])

    
    @property
    def get_delete_url(self):
        return reverse('lancamento_delete', args=[str(self.id)])

