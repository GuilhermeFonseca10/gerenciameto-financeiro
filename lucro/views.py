from django.db.models import Sum
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from conta.views import Conta
from lancamento.models import Lancamento
from lucro.forms import LucroForm
from lucro.models import Lucro
from utils.decorators import LoginRequiredMixin


class LucroListView(LoginRequiredMixin, ListView):
    model = Lucro

    def get_queryset(self):
        usuario = self.request.user

        return Lucro.objects.filter(usuario=usuario)

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context["total"] = (
            Lucro.objects.aggregate(valor_total=Sum("valor"))["valor_total"] or 0
           
        )
        return context


class LucroCreateView(LoginRequiredMixin, CreateView):
    model = Lucro

    form_class = LucroForm

    # fields = ['dispesa', 'valor', 'categorias', 'data', 'conta']

    success_url = "lucro_list"


class LucroUpdateView(LoginRequiredMixin, UpdateView):
    model = Lucro
    fields = ["ganhos", "valor", "data"]
    success_url = "lucro_list"


class LucroDeleteView(LoginRequiredMixin, DeleteView):
    model = Lucro
    success_url = "lucro_list"


# Create your views here.
