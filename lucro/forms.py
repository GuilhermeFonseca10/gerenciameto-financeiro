from crum import get_current_user
from django import forms

from .models import Conta, Lucro


class LucroForm(forms.ModelForm):
    class Meta:
        model = Lucro

        fields = ["ganhos", "valor", "data", "categorias", "conta"]

    def __init__(self, *args, **kwargs):
        super(LucroForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.initial["usuario"] = user.id
        contas = Conta.objects.filter(usuario=user)
        self.fields["conta"].queryset = contas

    