from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from utils.decorators import LoginRequiredMixin

from lancamento.models import Lancamento


class LancamentoListView(LoginRequiredMixin, ListView):
	model = Lancamento


class LancamentoCreateView(LoginRequiredMixin, CreateView):
	model = Lancamento
	fields = ['lancamento', 'valor', 'categorias', 'data']

	success_url = 'lancamento_list'


class LancamentoUpdateView(LoginRequiredMixin, UpdateView):
	model = Lancamento
	fields = ['lancamento', 'valor', 'categorias', 'data']
	success_url = 'lancamento_list'

class LancamentoDeleteView(LoginRequiredMixin, DeleteView):
	model = Lancamento
	success_url = 'lancamento_list'

# Create your views here.
