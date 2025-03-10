from django.db.models import Sum
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from conta.views import Conta
from lancamento.models import Lancamento
from lucro.forms import LucroForm
from lucro.models import Lucro
from utils.decorators import LoginRequiredMixin


class LucroListView(LoginRequiredMixin, ListView):
    model = Lucro

    def get_queryset(self):
        usuario = self.request.user
        print("Usuário autenticado:", usuario)
        return Lucro.objects.filter(usuario=usuario)

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context["total"] = (
            Lucro.objects.aggregate(valor_total=Sum("valor"))["valor_total"] or 0
           
        )
        print("Object List:", context["object_list"])
        return context


class LucroCreateView(LoginRequiredMixin, CreateView):
    model = Lucro
    form_class = LucroForm
    success_url = reverse_lazy("lucro_list")
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class LucroUpdateView(LoginRequiredMixin, UpdateView):
    model = Lucro
    fields = ["ganhos", "valor", "data"]
    success_url = reverse_lazy("lucro_list")


class LucroDeleteView(LoginRequiredMixin, DeleteView):
    model = Lucro
    success_url = reverse_lazy("lucro_list")


# Create your views here.
