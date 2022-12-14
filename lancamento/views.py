from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from conta.views import Conta
from lancamento.forms import LancamentoForm
from lancamento.models import Lancamento
from utils.decorators import LoginRequiredMixin


class LancamentoListView(LoginRequiredMixin, ListView):
    model = Lancamento

    def get_queryset(self):
        usuario = self.request.user

        return Lancamento.objects.filter(usuario=usuario)


class LancamentoCreateView(LoginRequiredMixin, CreateView):
    model = Lancamento

    form_class = LancamentoForm

    # fields = ['dispesa', 'valor', 'categorias', 'data', 'conta']

    success_url = "lancamento_list"


class LancamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Lancamento
    fields = ["dispesa", "categorias", "data"]
    success_url = "lancamento_list"


class LancamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Lancamento
    success_url = "lancamento_list"


# Create your views here.
