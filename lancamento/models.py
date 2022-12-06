from django.db import models
from categoria.models import Categoria
from django.core.urlresolvers import reverse
# Create your models here.
class Lancamento(models.Model):
    lancamento = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateField()
    
    categorias = models.ManyToManyField(Categoria)
    
    

    def __str__(self):
        return str(self.lancamento)

    def __unicode__(self):
        return '%s: R$ %d' % (self.lancamento, self.valor)

    class Meta:
        ordering = ['-valor','lancamento']


    @property
    def get_absolute_url(self):
        return reverse('lancamento_update', args=[str(self.id)])

    
    @property
    def get_delete_url(self):
        return reverse('lancamento_delete', args=[str(self.id)])


