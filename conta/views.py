# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from utils.decorators import LoginRequiredMixin
from conta.forms import ContaForm

from .models import Conta
from lancamento.views import Lancamento


class ContaListView(LoginRequiredMixin, ListView):
	model = Conta
	
	def get_queryset(self):
		usuario = self.request.user
		
		return Conta.objects.filter(usuario=usuario)
		#return Conta.objects.all()

class ContaCreateView(LoginRequiredMixin, CreateView):
	model = Conta
	def get_queryset(self):
		usuario = self.request.user
		
		
		return Conta.objects.filter(usuario=usuario)
	form_class = ContaForm
	
	success_url = 'conta_list'

	#def form_valid(self, form):
		#obj = form.save()
		#usuario = self.request.user.email
		#usuario.conta = obj
		#usuario.save()
		#return HttpResponse('ok')

class ContaUpdateView(LoginRequiredMixin, UpdateView):
	model = Conta
	fields = ['descricao', 'usuario']
	success_url = 'conta_list'

class ContaDeleteView(LoginRequiredMixin, DeleteView):
	model = Conta
	success_url = 'conta_list'

