from .models import Notificacao
from django.views.generic.base import TemplateView
from utils.decorators import LoginRequiredMixin


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):

    template_name = "core/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Buscar 3 notificações aleatórias
        context['notificacoes'] = Notificacao.objects.order_by('?')[:3]
        
        return context