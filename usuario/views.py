# views.py
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Usuario.objects.all()
        else:
            return Usuario.objects.filter(id=self.request.user.id)

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ["tipo", "username", "email", "password", "is_active"]
    success_url = reverse_lazy("usuario_list")
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("Você não tem permissão para acessar esta página.")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)  # Criptografa a senha
        user.save()
        return super().form_valid(form)

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ["username", "email"]
    success_url = reverse_lazy("usuario_list")
