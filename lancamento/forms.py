from crum import get_current_user
from django import forms
from django.forms.widgets import DateInput
from .models import Conta, Lancamento


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento

        fields = ["dispesa", "valor", "data", "categorias", "conta"]

    def __init__(self, *args, **kwargs):
        super(LancamentoForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.initial["usuario"] = user.id
        contas = Conta.objects.filter(usuario=user)
        self.fields["conta"].queryset = contas
    
        self.fields["data"].widget = DateInput(attrs={'type': 'date'})
