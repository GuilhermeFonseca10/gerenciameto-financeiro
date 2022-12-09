from django.shortcuts import render
from django.views.generic.base import TemplateView

from utils.decorators import LoginRequiredMixin
from lancamento.models import Lancamento
# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
	
	template_name = 'core/home.html'