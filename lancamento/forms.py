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
        self.fields["data"].widget = forms.DateInput(attrs={'type': 'date'})
