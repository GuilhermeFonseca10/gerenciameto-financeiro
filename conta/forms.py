from django import forms
from crum import get_current_user
from .models import Conta


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta

        fields = ['descricao', 'saldo', 'usuario']
    def __init__(self, *args, **kwargs):
        super(ContaForm, self).__init__(*args, **kwargs)
        self.initial["usuario"] = get_current_user().id
        #self.fields["usuario"].widget.attrs["disabled"] = True
