from django.db import models

class Notificacao(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )
    
    descricao = models.TextField(
        verbose_name='Descrição',
        max_length=500,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'core'
        verbose_name = 'Notificação para economizar'
        verbose_name_plural = 'Notificações para economizar'



