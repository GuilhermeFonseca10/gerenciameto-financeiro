from django.db.models import Q, Sum
# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator
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
    paginate_by = 2
    def get_queryset(self):
        usuario = self.request.user
        print("Usuário autenticado:", usuario)
        query = self.request.GET.get("q")
        if query:
            return Lucro.objects.filter(Q(usuario=usuario) & Q(ganhos__icontains=query))
        return Lucro.objects.filter(usuario=usuario)

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        context["total"] = (
            Lucro.objects.filter(usuario=usuario).aggregate(valor_total=Sum("valor"))["valor_total"] or 0
           
        )
        print("Object List:", context["object_list"])
        return context


class LucroCreateView(LoginRequiredMixin, CreateView):
    model = Lucro
    form_class = LucroForm
    success_url = reverse_lazy("lucro_list")
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        conta = form.instance.conta  # A conta associada ao lucro
        valor_lucro = form.cleaned_data['valor']  # O valor do lucro

        conta.saldo += valor_lucro
        conta.save()

        return super().form_valid(form)


class LucroUpdateView(LoginRequiredMixin, UpdateView):
    model = Lucro
    fields = ["ganhos", "valor", "data", "categorias", "conta"]
    template_name = "lucro/lucro_update.html"
    success_url = reverse_lazy("lucro_list")
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtra as contas para o usuário logado
        form.fields["conta"].queryset = Conta.objects.filter(usuario=self.request.user)
        return form

    def form_valid(self, form):
        lucro = self.get_object()  # Obtém o lucro antes da atualização
        conta = lucro.conta  

        valor_antigo = lucro.valor
        valor_novo = form.cleaned_data["valor"]
        diferenca = valor_novo - valor_antigo  # Calcula a diferença de valores

        conta.saldo += diferenca  # Ajusta o saldo da conta com a diferença
        conta.save()  # Atualiza o saldo da conta

        return super().form_valid(form)


class LucroDeleteView(LoginRequiredMixin, DeleteView):
    model = Lucro
    success_url = reverse_lazy("lucro_list")


# Create your views here.
