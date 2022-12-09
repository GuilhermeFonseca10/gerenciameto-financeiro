from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from utils.decorators import LoginRequiredMixin
from lucro.forms import LucroForm
from conta.views import Conta
from lucro.models import Lucro
from lancamento.models import Lancamento


class LucroListView(LoginRequiredMixin, ListView):
	model = Lucro
	
	def get_queryset(self):
		usuario = self.request.user
		
		return Lucro.objects.filter(usuario=usuario)
	
class LucroCreateView(LoginRequiredMixin, CreateView):
	model = Lucro
	
	form_class = LucroForm
	
	
	#fields = ['dispesa', 'valor', 'categorias', 'data', 'conta']
	

	success_url = 'lucro_list'
	

class LucroUpdateView(LoginRequiredMixin, UpdateView):
	model = Lucro
	fields = ['ganhos', 'valor', 'data']
	success_url = 'lucro_list'

class LucroDeleteView(LoginRequiredMixin, DeleteView):
	model = Lucro
	success_url = 'lucro_list'

# Create your views here.
