from crum import get_current_user
from django import forms

from .models import Conta


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta

        fields = ["nome", "saldo", "usuario"]

    def __init__(self, *args, **kwargs):
        super(ContaForm, self).__init__(*args, **kwargs)
        current_user = get_current_user()
        if current_user:
            self.initial["usuario"] = current_user.id
        else:
            raise ValueError("Usuário não autenticado.")
