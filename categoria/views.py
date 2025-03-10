# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from utils.decorators import LoginRequiredMixin

from .models import Categoria


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ["descricao"]
    success_url = reverse_lazy("categoria_list")


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ["descricao"]
    success_url = reverse_lazy("categoria_list")


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy("categoria_list")
