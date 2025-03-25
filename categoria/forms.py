from crum import get_current_user
from django import forms

from .models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = ["descricao", "usuario"]

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        current_user = get_current_user()
        if current_user:
            self.initial["usuario"] = current_user.id
        else:
            raise ValueError("Usuário não autenticado.")
