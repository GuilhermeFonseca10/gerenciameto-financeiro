# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from utils.decorators import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Categoria
from lancamento.models import Lancamento
from lucro.models import Lucro


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    paginate_by = 2
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Categoria.objects.filter(Q(descricao__icontains=query))
        return Categoria.objects.all()


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
    
class DespesasPorCategoriaView(LoginRequiredMixin, ListView):
    template_name = "categoria/despesas_por_categoria.html"
    context_object_name = "despesas"

    def get_queryset(self):
        categoria_id = self.kwargs["pk"]
        return Lancamento.objects.filter(categorias__id=categoria_id, usuario=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs["pk"]
        context['categoria'] = Categoria.objects.get(id=categoria_id)  # Obtém a categoria com o id
        return context

class LucrosPorCategoriaView(LoginRequiredMixin, ListView):
    template_name = "categoria/lucros_por_categoria.html"
    context_object_name = "lucros"

    def get_queryset(self):
        categoria_id = self.kwargs["pk"]
        return Lucro.objects.filter(categorias__id=categoria_id, usuario=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs["pk"]
        context['categoria'] = Categoria.objects.get(id=categoria_id)  # Obtém a categoria com o id
        return context

