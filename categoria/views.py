# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from utils.decorators import LoginRequiredMixin
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from .models import Categoria
from lancamento.models import Lancamento
from lucro.models import Lucro
from categoria.forms import CategoriaForm


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    paginate_by = 10
    def get_queryset(self):
        usuario = self.request.user
        query = self.request.GET.get("q")
        if query:
            return Categoria.objects.filter(Q(usuario=usuario) & Q(descricao__icontains=query))
        return Categoria.objects.filter(usuario=usuario)


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    
    def get_queryset(self):
        usuario = self.request.user

        return Categoria.objects.filter(usuario=usuario)

    form_class = CategoriaForm
    success_url = reverse_lazy("categoria_list")


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ["descricao", "usuario"]
    success_url = reverse_lazy("categoria_list")


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    
    success_url = reverse_lazy("categoria_list")
    
class DespesasPorCategoriaView(LoginRequiredMixin, ListView):
    template_name = "categoria/despesas_por_categoria.html"
    paginate_by = 10
    context_object_name = "despesas"

    def get_queryset(self):
        categoria_id = self.kwargs["pk"]
        usuario = self.request.user
        query = self.request.GET.get("q")  # Captura o termo de busca
        
        queryset = Lancamento.objects.filter(categorias__id=categoria_id, usuario=usuario)

        if query:
            queryset = queryset.filter(Q(dispesa__icontains=query))  # Filtra pelo nome da despesa

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs["pk"]
        
        context['categoria'] = Categoria.objects.get(id=categoria_id)  # Obtém a categoria
        
        # Filtrando os lançamentos com base na pesquisa
        despesas = self.get_queryset()
        
        # Calculando o total das despesas filtradas
        total_despesas = despesas.aggregate(total=Sum('valor'))['total'] or 0

        context['total_despesas'] = total_despesas
        context['query'] = self.request.GET.get("q", "")  # Mantém o termo de pesquisa no template
        
        return context
class LucrosPorCategoriaView(LoginRequiredMixin, ListView):
    template_name = "categoria/lucros_por_categoria.html"
    context_object_name = "lucros"
    paginate_by = 10

    def get_queryset(self):
        categoria_id = self.kwargs["pk"]
        usuario = self.request.user
        query = self.request.GET.get("q")  # Captura o termo de busca
        
        queryset = Lucro.objects.filter(categorias__id=categoria_id, usuario=usuario)

        if query:
            queryset = queryset.filter(Q(ganhos__icontains=query))  # Filtra pelo nome do ganho

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.kwargs["pk"]
        
        context['categoria'] = Categoria.objects.get(id=categoria_id)  # Obtém a categoria
        
        # Filtrando os lançamentos com base na pesquisa
        lucros = self.get_queryset()
        
        # Calculando o total das despesas filtradas
        total_lucros = lucros.aggregate(total=Sum('valor'))['total'] or 0

        context['total_lucros'] = total_lucros
        context['query'] = self.request.GET.get("q", "")  # Mantém o termo de pesquisa no template
        
        return context

