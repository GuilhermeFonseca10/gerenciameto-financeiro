from crum import get_current_user
from django import forms
from django.forms.widgets import DateInput
from .models import Conta, Lucro


class LucroForm(forms.ModelForm):
    class Meta:
        model = Lucro
        fields = ["ganhos", "valor", "data", "categorias", "conta"]

    def __init__(self, *args, **kwargs):
        super(LucroForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        if user:
            contas = Conta.objects.filter(usuario=user)
            self.fields["conta"].queryset = contas

        self.fields["data"].widget = DateInput(attrs={'type': 'date'})