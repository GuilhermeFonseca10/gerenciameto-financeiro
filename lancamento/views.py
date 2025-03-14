from django.db.models import Sum
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from lancamento.forms import LancamentoForm
from lancamento.models import Lancamento
from utils.decorators import LoginRequiredMixin
from django.contrib import messages
from .models import Conta
class LancamentoListView(LoginRequiredMixin, ListView):
    model = Lancamento

    def get_queryset(self):
        usuario = self.request.user

        return Lancamento.objects.filter(usuario=usuario)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        # Calcular o total de despesas do usuário
        total_gastos = Lancamento.objects.filter(usuario=usuario).aggregate(total=Sum('valor'))['total'] or 0
        context['total_gastos'] = total_gastos
        return context


class LancamentoCreateView(LoginRequiredMixin, CreateView):
    model = Lancamento

    form_class = LancamentoForm

    # fields = ['dispesa', 'valor', 'categorias', 'data', 'conta']

    success_url = reverse_lazy ("lancamento_list")
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtra as contas para o usuário logado
        form.fields["conta"].queryset = Conta.objects.filter(usuario=self.request.user)
        return form
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        conta = form.instance.conta  # A conta associada ao lançamento
        valor_lancamento = form.cleaned_data['valor']  # O valor da despesa

        # Subtrai o valor do lançamento do saldo da conta, mesmo que fique negativo
        conta.saldo -= valor_lancamento
        conta.save()

        # Verificar se o saldo ficou negativo e mostrar uma mensagem para o usuário
        if conta.saldo < 0:
            messages.warning(self.request, "Alerta: Seu saldo ficou negativo devido ao lançamento. O valor excedeu o limite disponível da conta.")

        # Salva o lançamento no banco de dados
        return super().form_valid(form)

    def form_invalid(self, form):
        # Caso o formulário seja inválido, redireciona de volta ao formulário com erros
        messages.error(self.request, "Houve um erro ao salvar o lançamento. Tente novamente.")
        return super().form_invalid(form)


class LancamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Lancamento
    fields = ["dispesa", "valor", "categorias", "data", "conta"]
    template_name = "lancamento/lancamento_update.html"
    success_url = reverse_lazy ("lancamento_list")
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtra as contas para o usuário logado
        form.fields["conta"].queryset = Conta.objects.filter(usuario=self.request.user)
        return form

    def form_valid(self, form):
        lancamento = self.get_object()  # Obtém o lançamento antes da atualização
        conta = lancamento.conta  

        # Reverte o saldo anterior antes de aplicar o novo valor
        conta.saldo += lancamento.valor  # Devolve o valor antigo
        conta.saldo -= form.cleaned_data["valor"]  # Subtrai o novo valor

        conta.save()  # Atualiza o saldo da conta

        return super().form_valid(form)

class LancamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Lancamento
    success_url = reverse_lazy ("lancamento_list")
    


# Create your views here.
