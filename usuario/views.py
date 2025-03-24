# views.py
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    paginate_by = 2
    def get_queryset(self):
        if self.request.user.is_superuser:
            query = self.request.GET.get("q")
            if query:
                return Usuario.objects.filter(Q(username__icontains=query) or Q(email__icontains=query))
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
    
class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy("usuario_list")
