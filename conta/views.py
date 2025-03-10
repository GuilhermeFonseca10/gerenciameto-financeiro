# coding: utf-8
from django.db.models import Sum
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from conta.models import Conta
from conta.forms import ContaForm
from lancamento.views import Lancamento
from utils.decorators import LoginRequiredMixin
from django.urls import reverse_lazy

class ContaListView(LoginRequiredMixin, ListView):
    model = Conta

    def get_queryset(self):
        usuario = self.request.user

        return Conta.objects.filter(usuario=usuario)
        # return Conta.objects.all()


class ContaCreateView(LoginRequiredMixin, CreateView):
    model = Conta

    def get_queryset(self):
        usuario = self.request.user

        return Conta.objects.filter(usuario=usuario)

    form_class = ContaForm

    success_url = reverse_lazy("conta_list")

    # def form_valid(self, form):
    # obj = form.save()
    # usuario = self.request.user.email
    # usuario.conta = obj
    # usuario.save()
    # return HttpResponse('ok')


class ContaUpdateView(LoginRequiredMixin, UpdateView):
    model = Conta
    fields = ["descricao"]
    success_url = reverse_lazy("conta_list")


class ContaDeleteView(LoginRequiredMixin, DeleteView):
    model = Conta
    success_url = reverse_lazy("conta_list")
