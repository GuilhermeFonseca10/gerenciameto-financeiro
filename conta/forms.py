from crum import get_current_user
from django import forms

from .models import Conta


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta

        fields = ["descricao", "saldo", "usuario"]

    def __init__(self, *args, **kwargs):
        super(ContaForm, self).__init__(*args, **kwargs)
        current_user = get_current_user()
        if current_user:
            self.initial["usuario"] = current_user.id
        else:
            # Se o usuário não estiver autenticado, você pode optar por lançar uma exceção,
            # ou lidar com o caso de outra forma (por exemplo, redirecionando o usuário)
            raise ValueError("Usuário não autenticado.")
