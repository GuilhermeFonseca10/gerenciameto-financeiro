# coding: utf-8
from django.db import models
from django.urls import reverse


class Categoria(models.Model):

    descricao = models.CharField("descrição", max_length=40, unique=True)

    def __str__(self):
        return str(self.descricao)

    class Meta:
        ordering = ["descricao"]

    def __unicode__(self):
        self.descricao

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        super(Categoria, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse("categoria_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("categoria_delete", args=[str(self.id)])
