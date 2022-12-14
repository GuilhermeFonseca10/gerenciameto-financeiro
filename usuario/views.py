# coding: utf-8
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from utils.decorators import LoginRequiredMixin

from .models import Usuario


class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario

    def get_queryset(self):
        usuario_id = self.request.user.id

        return Usuario.objects.filter(id=usuario_id)


class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ["tipo", "username", "email", "password", "is_active"]
    success_url = "usuario_list"


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ["username", "email"]
    success_url = "usuario_list"


# class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
# model = Usuario
# success_url = 'usuario_list'
