from django.shortcuts import render
from django.views.generic.base import TemplateView

from lancamento.models import Lancamento
from utils.decorators import LoginRequiredMixin


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):

    template_name = "core/home.html"
    
